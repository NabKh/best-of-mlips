"""Rebuild README.md, data/models.json and the figures.

Benchmark numbers, licenses and training sets come from the Matbench Discovery
model files (github.com/janosh/matbench-discovery, MIT). Loading snippets and the
models outside that benchmark come from data/families.yaml and data/beyond_pbe.yaml.

    python scripts/build.py                  # clone Matbench Discovery, query GitHub stars
    python scripts/build.py --mbd PATH       # use an existing checkout
    python scripts/build.py --offline        # keep the stars from data/models.json
"""

import argparse
import datetime as dt
import json
import os
import re
import subprocess
import tempfile
import urllib.request
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.dates as mdates
import matplotlib.pyplot as plt
import matplotlib.ticker
import yaml
from adjustText import adjust_text

ROOT = Path(__file__).resolve().parents[1]
MBD_URL = "https://github.com/janosh/matbench-discovery"
MBD_SITE = "https://matbench-discovery.materialsproject.org"
TODAY = dt.datetime.now(dt.timezone.utc).date()

PERMISSIVE = {"MIT", "BSD-3-Clause", "Apache-2.0", "CC-BY-4.0"}
COPYLEFT = {"GPL-3.0", "LGPL-3.0"}
NON_COMMERCIAL = {"ASL", "CC-BY-NC-4.0", "CC-BY-NC-SA-4.0"}
LICENSE_CLASSES = {
    "permissive": ("🟢", "permissive (MIT, BSD, Apache, CC-BY)"),
    "copyleft": ("🟡", "copyleft (GPL, LGPL): share changes under the same license"),
    "non-commercial": ("🔴", "academic / non-commercial use only"),
    "custom": ("⚪", "custom license: read it before use"),
}
MP_FAMILY = {"MPtrj", "MPF", "MP 2022", "MP Graphs", "MDR-MP PBE ω_q"}
ALEX_FAMILY = {"Alex", "sAlex", "OMat24"}
GROUPS = {
    "mp": ("MPtrj only", "#0072B2"),
    "alex": ("MPtrj + Alexandria / OMat24", "#D55E00"),
    "other": ("other or in-house data", "#009E73"),
}
MARKERS = {"permissive": "o", "copyleft": "s", "non-commercial": "X", "custom": "D"}


def license_class(name):
    if name in PERMISSIVE:
        return "permissive"
    if name in COPYLEFT:
        return "copyleft"
    if name in NON_COMMERCIAL:
        return "non-commercial"
    return "custom"


def data_group(sets):
    if set(sets) & ALEX_FAMILY and set(sets) <= MP_FAMILY | ALEX_FAMILY:
        return "alex"
    if set(sets) <= MP_FAMILY:
        return "mp"
    return "other"


def github_slug(url):
    m = re.match(r"https://github\.com/([^/]+/[^/#?]+)", url or "")
    return m.group(1).removesuffix(".git") if m else None


def clone_mbd(dest):
    subprocess.run(
        ["git", "clone", "-q", "--depth", "1", "--filter=blob:none", "--sparse", MBD_URL, str(dest)], check=True
    )
    subprocess.run(["git", "-C", str(dest), "sparse-checkout", "set", "models", "data"], check=True)


def load_models(mbd):
    datasets = yaml.safe_load((mbd / "data" / "datasets.yml").read_text())
    overrides = yaml.safe_load((ROOT / "data" / "license_overrides.yaml").read_text()) or {}
    models = []
    for path in sorted((mbd / "models").glob("*/*.yml")):
        d = yaml.safe_load(path.read_text())
        targets = str(d.get("targets", ""))
        lic = dict(d.get("license", {}))
        fix = overrides.get(d["model_key"])
        if fix:
            lic.update(checkpoint=fix["license"], checkpoint_url=fix["url"])
        if d.get("lifecycle") != "active" or "F" not in targets.split("_")[0]:
            continue  # energy-only models, superseded and aborted runs
        if lic.get("checkpoint") == "unreleased":
            continue
        metrics = d.get("metrics") or {}
        discovery = metrics.get("discovery") if isinstance(metrics.get("discovery"), dict) else {}
        phonons = metrics.get("phonons") if isinstance(metrics.get("phonons"), dict) else {}
        geo = metrics.get("geo_opt") if isinstance(metrics.get("geo_opt"), dict) else {}
        kappa = phonons.get("kappa_103") if isinstance(phonons.get("kappa_103"), dict) else {}
        rmsd = (geo.get("symprec=1e-5") or {}).get("rmsd") if isinstance(geo.get("symprec=1e-5"), dict) else None
        sets = d.get("training_sets") or []
        if isinstance(sets, dict):
            sets = list(sets)
        dates = d.get("dates") or {}
        date = dates.get("benchmark_added") or dates.get("paper_published")
        functionals = sorted({_functional(datasets, s) for s in sets})
        models.append(
            {
                "key": d["model_key"],
                "name": d["model_name"],
                "family": path.parent.name,
                "date": str(date) if date else None,
                "params": d.get("model_params"),
                "training_sets": sets,
                "training_structures": sum((datasets.get(s) or {}).get("n_structures", 0) for s in sets),
                "reference_functional": functionals,
                "data_group": data_group(sets),
                "forces": "conservative" if "G" in targets.split("_")[-1] else "direct",
                "repo": d.get("repo"),
                "paper": d.get("paper") or d.get("doi"),
                "pypi": d.get("pypi"),
                "checkpoint_url": d.get("checkpoint_url"),
                "license_code": lic.get("code"),
                "license_code_url": lic.get("code_url"),
                "license_weights": lic.get("checkpoint"),
                "license_weights_url": lic.get("checkpoint_url"),
                "license_class": license_class(lic.get("checkpoint")),
                "license_note": fix["note"] if fix else None,
                "F1": (discovery.get("full_test_set") or {}).get("F1"),
                "kappa_SRME": kappa.get("κ_SRME"),
                "RMSD": rmsd,
                "source": f"{MBD_URL}/blob/main/models/{path.parent.name}/{path.name}",
            }
        )
    return models, datasets


def _functional(datasets, name):
    entry = datasets.get(name) or {}
    functional = (entry.get("params") or {}).get("functional")
    if not functional and entry.get("contains"):  # subsets inherit from their parent set
        return _functional(datasets, entry["contains"][0])
    return str(functional or "?")


def fetch_stars(models, previous):
    token = os.environ.get("GITHUB_TOKEN")
    stars = {}
    for slug in sorted({github_slug(m["repo"]) for m in models} - {None}):
        req = urllib.request.Request(f"https://api.github.com/repos/{slug}")
        req.add_header("Accept", "application/vnd.github+json")
        if token:
            req.add_header("Authorization", f"Bearer {token}")
        try:
            with urllib.request.urlopen(req, timeout=20) as r:
                stars[slug] = json.load(r)["stargazers_count"]
        except (OSError, KeyError, ValueError) as e:  # keep the last known value
            print(f"stars for {slug}: {e}")
            if slug in previous:
                stars[slug] = previous[slug]
    return stars


# ---------------------------------------------------------------- figures


def style(dark):
    fg, grid = ("#c9d1d9", "#30363d") if dark else ("#24292f", "#d0d7de")
    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "font.size": 10,
            "text.color": fg,
            "axes.labelcolor": fg,
            "axes.edgecolor": grid,
            "xtick.color": fg,
            "ytick.color": fg,
            "axes.grid": True,
            "grid.color": grid,
            "grid.linewidth": 0.6,
            "axes.spines.top": False,
            "axes.spines.right": False,
            "figure.facecolor": "none",
            "axes.facecolor": "none",
            "savefig.facecolor": "none",
            "legend.frameon": False,
            "svg.fonttype": "none",
            "svg.hashsalt": "foundation-mlips",
        }
    )
    return fg


def legend_handles(fg, groups=True, licenses=True):
    from matplotlib.lines import Line2D

    handles = []
    if groups:
        handles += [
            Line2D([], [], ls="", marker="o", color=c, label=label, markersize=7) for label, c in GROUPS.values()
        ]
    if licenses:
        handles += [
            Line2D([], [], ls="", marker=MARKERS[k], mfc="none", mec=fg, label=f"weights: {k}", markersize=7)
            for k in LICENSE_CLASSES
        ]
    return handles


def scatter(ax, models, x, y):
    for m in models:
        ax.scatter(
            m[x] if x != "date" else dt.date.fromisoformat(m["date"]),
            m[y],
            s=55,
            marker=MARKERS[m["license_class"]],
            color=GROUPS[m["data_group"]][1],
            edgecolor="white",
            linewidth=0.6,
            alpha=0.9,
            zorder=3,
        )


def fig_pareto(models, dark):
    fg = style(dark)
    pts = [m for m in models if m["F1"] is not None and m["kappa_SRME"] is not None]
    fig, ax = plt.subplots(figsize=(9, 6))
    scatter(ax, pts, "kappa_SRME", "F1")
    front, best = [], -1
    for m in sorted(pts, key=lambda m: m["kappa_SRME"]):
        if m["F1"] > best:
            front.append(m)
            best = m["F1"]
    ax.plot([m["kappa_SRME"] for m in front], [m["F1"] for m in front], color=fg, lw=1, ls="--", zorder=2)
    family_best = {
        max((m for m in pts if m["family"] == f), key=lambda m: m["F1"])["key"] for f in {m["family"] for m in pts}
    }
    crowded = {m["key"] for m in pts if m["F1"] > 0.88 and m["kappa_SRME"] < 0.25}  # leaderboard top; see table
    labels = {m["key"] for m in front} | (family_best - crowded)
    texts = [ax.text(m["kappa_SRME"], m["F1"], m["name"], fontsize=7.5, color=fg) for m in pts if m["key"] in labels]
    adjust_text(texts, ax=ax, arrowprops={"arrowstyle": "-", "color": fg, "lw": 0.4})
    ax.set_xlabel("κ$_\\mathrm{SRME}$: thermal-conductivity error from phonons   (lower is better →)")
    ax.set_ylabel("F1: finds stable crystals   (higher is better ↑)")
    ax.set_xscale("log")
    ax.xaxis.set_major_formatter(matplotlib.ticker.FormatStrFormatter("%g"))
    ax.set_xticks([0.05, 0.1, 0.2, 0.5, 1, 2])
    ax.invert_xaxis()
    ax.legend(handles=legend_handles(fg), loc="lower right", fontsize=8)
    ax.set_title(
        "Stability screening vs. phonons; dashed line = best trade-off, unlabelled top-right cluster in the table",
        loc="left",
        fontsize=10,
    )
    return fig


def fig_timeline(models, dark):
    fg = style(dark)
    pts = sorted((m for m in models if m["F1"] is not None and m["date"]), key=lambda m: m["date"])
    fig, ax = plt.subplots(figsize=(9, 4.2))
    scatter(ax, pts, "date", "F1")
    best, xs, ys = 0, [], []
    for m in pts:
        best = max(best, m["F1"])
        xs.append(dt.date.fromisoformat(m["date"]))
        ys.append(best)
    xs.append(TODAY)
    ys.append(best)
    ax.step(xs, ys, where="post", color=fg, lw=1, ls="--", zorder=2)
    best, texts = 0, []
    for m in pts:
        if m["F1"] > best + 0.005:
            best = m["F1"]
            texts.append(ax.text(dt.date.fromisoformat(m["date"]), m["F1"], m["name"], fontsize=7.5, color=fg))
    adjust_text(texts, ax=ax, arrowprops={"arrowstyle": "-", "color": fg, "lw": 0.4})
    ax.xaxis.set_major_locator(mdates.YearLocator())
    ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.set_ylabel("F1 (stable-crystal discovery)")
    ax.legend(handles=legend_handles(fg, licenses=False), loc="lower right", fontsize=8)
    ax.set_title("Release date vs. accuracy; dashed line = best so far", loc="left", fontsize=10)
    return fig


def fig_size(models, dark):
    fg = style(dark)
    pts = [m for m in models if m["F1"] is not None and m["params"]]
    fig, ax = plt.subplots(figsize=(9, 4.2))
    scatter(ax, pts, "params", "F1")
    ax.set_xscale("log")
    ax.set_xlabel("trainable parameters")
    ax.set_ylabel("F1")
    texts = [
        ax.text(m["params"], m["F1"], m["name"], fontsize=7, color=fg)
        for m in pts
        if m["params"] < 2e6 or m["params"] > 1e8
    ]
    adjust_text(texts, ax=ax, arrowprops={"arrowstyle": "-", "color": fg, "lw": 0.4})
    ax.legend(handles=legend_handles(fg, licenses=False), loc="lower right", fontsize=8)
    ax.set_title("Model size vs. accuracy; colour = training data", loc="left", fontsize=10)
    return fig


def fig_datasets(models, datasets, dark):
    fg = style(dark)
    used = {}
    for m in models:
        for s in m["training_sets"]:
            used[s] = used.get(s, 0) + 1
    names = sorted(used, key=lambda s: (datasets.get(s) or {}).get("n_structures", 0))
    fig, ax = plt.subplots(figsize=(9, 0.42 * len(names) + 1))
    sizes = [(datasets.get(s) or {}).get("n_structures", 0) for s in names]
    ax.barh(names, sizes, color="#56B4E9")
    for i, s in enumerate(names):
        ax.text(
            sizes[i] * 1.15,
            i,
            f"{_functional(datasets, s)}  ·  used by {used[s]} model{'s' if used[s] > 1 else ''}",
            va="center",
            fontsize=8,
            color=fg,
        )
    ax.set_xscale("log")
    ax.set_xlim(right=max(sizes) * 40)
    ax.set_xlabel("DFT structures in the training set")
    ax.grid(axis="y", visible=False)
    ax.set_title("What these models learned from, and at which level of theory", loc="left", fontsize=10)
    return fig


def save_figures(models, datasets):
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    makers = {
        "pareto": fig_pareto,
        "timeline": fig_timeline,
        "size": fig_size,
        "datasets": lambda m, d: fig_datasets(m, datasets, d),
    }
    for name, make in makers.items():
        for dark in (False, True):
            fig = make(models, dark)
            fig.tight_layout()
            fig.savefig(out / f"{name}{'-dark' if dark else ''}.svg", metadata={"Date": None})
            plt.close(fig)


# ---------------------------------------------------------------- README


def picture(name, alt):
    return (
        "<picture>\n"
        f'  <source media="(prefers-color-scheme: dark)" srcset="figures/{name}-dark.svg">\n'
        f'  <img src="figures/{name}.svg" alt="{alt}" width="100%">\n'
        "</picture>"
    )


def fmt_params(n):
    if not n:
        return "–"
    return f"{n / 1e6:.0f} M" if n >= 1e7 else f"{n / 1e6:.1f} M"


def fmt(value, digits=3):
    return "–" if value is None else f"{value:.{digits}f}"


def leaderboard(models, stars):
    rows = sorted(models, key=lambda m: -(m["F1"] or 0))
    top = {
        "F1": sorted(m["F1"] for m in rows if m["F1"] is not None)[-3:],
        "kappa_SRME": sorted(m["kappa_SRME"] for m in rows if m["kappa_SRME"] is not None)[:3],
        "RMSD": sorted(m["RMSD"] for m in rows if m["RMSD"] is not None)[:3],
    }

    def cell(m, key, digits=3):
        text = fmt(m[key], digits)
        return f"**{text}**" if m[key] is not None and m[key] in top[key] else text

    lines = [
        "| Model | Benchmarked | Size | Training data | Forces | F1 ↑ | κ<sub>SRME</sub> ↓ | RMSD ↓ | Weights license | ⭐ |",
        "|---|---|---:|---|---|---:|---:|---:|---|---:|",
    ]
    for m in rows:
        slug = github_slug(m["repo"])
        star = f"[{stars[slug]:,}]({m['repo']})" if slug in stars else "–"
        icon = LICENSE_CLASSES[m["license_class"]][0]
        lic = m["license_weights"] or "?"
        lic = f"{icon} [{lic}]({m['license_weights_url']})" if m["license_weights_url"] else f"{icon} {lic}"
        if m["license_note"]:
            lic += " [†](#license-corrections)"
        data = f"{', '.join(m['training_sets'])} <sub>{' / '.join(m['reference_functional'])}</sub>"
        name = f"[{m['name']}]({m['paper']})" if m["paper"] else m["name"]
        forces = "conservative" if m["forces"] == "conservative" else "**direct**"
        lines.append(
            f"| {name} | {(m['date'] or '–')[:7]} | {fmt_params(m['params'])} | {data} "
            f"| {forces} | {cell(m, 'F1')} | {cell(m, 'kappa_SRME')} | {cell(m, 'RMSD', 4)} | {lic} | {star} |"
        )
    return "\n".join(lines)


def license_corrections(models):
    notes = {}
    for m in models:
        if m["license_note"]:
            notes.setdefault((m["license_note"], m["license_weights_url"]), []).append(m["name"])
    return "\n".join(f"- {', '.join(names)}: {note} [Source]({url})." for (note, url), names in notes.items())


def license_legend():
    return " · ".join(f"{icon} {text}" for icon, text in LICENSE_CLASSES.values())


def snippets(families):
    blocks = []
    for f in families:
        body = [f"<details>\n<summary><b>{f['name']}</b> · {f['models']}</summary>\n"]
        if f.get("install"):
            body.append(f"```bash\n{f['install'].strip()}\n```\n")
        if f.get("snippet"):
            body.append(f"```python\n{f['snippet'].strip()}\n```\n")
        if f.get("notes"):
            body.append(f"{f['notes'].strip()}\n")
        body.append(f"Source: [{f['source_label']}]({f['source']})\n</details>")
        blocks.append("\n".join(body))
    return "\n\n".join(blocks)


def beyond_table(entries):
    lines = [
        "| Model | Domain | Reference level of theory | Training data | Weights license | Paper |",
        "|---|---|---|---|---|---|",
    ]
    for e in entries:
        icon = LICENSE_CLASSES[e["license_class"]][0]
        lic = f"{icon} [{e['license']}]({e['license_url']})" if e.get("license_url") else f"{icon} {e['license']}"
        name = f"[{e['name']}]({e['repo']})" if e.get("repo") else e["name"]
        lines.append(
            f"| {name} | {e['domain']} | {e['theory']} | {e['data']} | {lic} | [{e['paper_label']}]({e['paper']}) |"
        )
    return "\n".join(lines)


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--mbd", type=Path, help="existing matbench-discovery checkout")
    parser.add_argument("--offline", action="store_true", help="do not query GitHub for stars")
    args = parser.parse_args(argv)

    snapshot = ROOT / "data" / "models.json"
    previous = json.loads(snapshot.read_text()).get("stars", {}) if snapshot.exists() else {}

    with tempfile.TemporaryDirectory() as tmp:
        mbd = args.mbd
        if mbd is None:
            mbd = Path(tmp) / "matbench-discovery"
            clone_mbd(mbd)
        commit = subprocess.run(
            ["git", "-C", str(mbd), "rev-parse", "HEAD"], capture_output=True, text=True, check=True
        ).stdout.strip()
        models, datasets = load_models(mbd)

    stars = previous if args.offline else fetch_stars(models, previous)
    families = yaml.safe_load((ROOT / "data" / "families.yaml").read_text())
    beyond = yaml.safe_load((ROOT / "data" / "beyond_pbe.yaml").read_text())

    save_figures(models, datasets)
    snapshot.write_text(
        json.dumps(
            {"matbench_discovery_commit": commit, "stars": stars, "models": models}, indent=1, ensure_ascii=False
        )
        + "\n"
    )

    template = (ROOT / "scripts" / "template.md").read_text()
    readme = template
    for key, value in {
        "N_MODELS": str(len(models)),
        "N_FAMILIES": str(len({m["family"] for m in models})),
        "UPDATED": TODAY.isoformat(),
        "UPDATED_BADGE": TODAY.isoformat().replace("-", "--"),
        "MBD_URL": MBD_URL,
        "MBD_SITE": MBD_SITE,
        "MBD_COMMIT": f"[`{commit[:7]}`]({MBD_URL}/tree/{commit})",
        "LEADERBOARD": leaderboard(models, stars),
        "LICENSE_LEGEND": license_legend(),
        "LICENSE_CORRECTIONS": license_corrections(models),
        "SNIPPETS": snippets(families),
        "BEYOND_PBE": beyond_table(beyond),
        "FIG_PARETO": picture("pareto", "F1 versus thermal conductivity error for each model"),
        "FIG_TIMELINE": picture("timeline", "F1 of each model against its release date"),
        "FIG_SIZE": picture("size", "F1 against number of parameters"),
        "FIG_DATASETS": picture("datasets", "Size and level of theory of each training set"),
    }.items():
        readme = readme.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", readme)
    if leftover:
        raise SystemExit(f"unfilled placeholders: {leftover}")
    (ROOT / "README.md").write_text(readme)
    print(f"{len(models)} models, {len(stars)} repos with stars, Matbench Discovery {commit[:7]}")


if __name__ == "__main__":
    main()
