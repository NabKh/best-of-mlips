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
import matplotlib.pyplot as plt
import yaml

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


FONTS = ["Arial", "Liberation Sans", "DejaVu Sans"]  # first one installed wins; Liberation Sans has Arial metrics
GROUP_STYLE = {
    "mp": ("#2F6FB3", "MPtrj only"),
    "alex": ("#E0662A", "MPtrj + Alexandria and/or OMat24"),
    "other": ("#1A9E77", "other training sets"),
}
INK, MUTED, GRID, BAND = "#1D2330", "#6B7280", "#E5E7EB", "#F5F6F8"
PANELS = [  # key, title, subtitle, x range, ticks
    ("F1", "F1", "stable-crystal classification · higher is better", (0.55, 0.935), [0.6, 0.7, 0.8, 0.9]),
    (
        "kappa_SRME",
        "κ$_\\mathbf{SRME}$",
        "phonon thermal-conductivity error · lower is better",
        (0, 2.0),
        [0, 0.5, 1, 1.5, 2],
    ),
    ("RMSD", "RMSD", "relaxed vs. DFT structure · lower is better", (0.05, 0.12), [0.06, 0.08, 0.10, 0.12]),
]


def fig_hero(models, commit):
    """Every model ranked by F1, with its three Matbench Discovery metrics side by side."""
    from matplotlib import font_manager
    from matplotlib.lines import Line2D

    installed = {f.name for f in font_manager.fontManager.ttflist}
    font = next(f for f in FONTS if f in installed)
    plt.rcParams.update(
        {
            "font.family": font,
            "mathtext.fontset": "custom",
            "mathtext.rm": font,
            "mathtext.it": f"{font}:italic",
            "mathtext.bf": f"{font}:bold",
            "svg.fonttype": "path",
            "svg.hashsalt": "foundation-mlips",
            "xtick.color": MUTED,
            "ytick.color": INK,
            "xtick.labelsize": 9,
            "ytick.labelsize": 9.5,
        }
    )
    models = sorted((m for m in models if m["F1"] is not None), key=lambda m: m["F1"])
    n = len(models)
    fig, axes = plt.subplots(
        1, 3, figsize=(12, 0.27 * n + 2.6), sharey=True, gridspec_kw={"width_ratios": [1.25, 1.1, 1], "wspace": 0.06}
    )
    for ax, (key, title, sub, (lo, hi), ticks) in zip(axes, PANELS):
        best = sorted((m[key] for m in models if m[key] is not None), reverse=key == "F1")[:3]
        for y, m in enumerate(models):
            if y % 2:
                ax.axhspan(y - 0.5, y + 0.5, color=BAND, zorder=0, lw=0)
            v = m[key]
            if v is None:
                ax.text(lo + 0.01 * (hi - lo), y, "not tested", va="center", fontsize=7.5, color=MUTED)
                continue
            c = GROUP_STYLE[m["data_group"]][0]
            ax.plot([lo, v], [y, y], color=c, lw=1.4, alpha=0.35, solid_capstyle="round", zorder=2)
            ax.scatter(v, y, s=46, zorder=3, color="white" if m["forces"] == "direct" else c, edgecolor=c, lw=1.6)
            top = v in best
            ax.text(
                v + 0.025 * (hi - lo),
                y,
                f"{v:.4f}" if key == "RMSD" else f"{v:.3f}",
                va="center",
                fontsize=7.5,
                color=INK if top else MUTED,
                fontweight="bold" if top else "normal",
            )
        ax.set_xlim(lo, hi)
        ax.set_xticks(ticks)
        ax.tick_params(length=0)
        ax.tick_params(axis="x", pad=2)
        ax.grid(axis="x", color=GRID, lw=0.8, zorder=1)
        ax.set_axisbelow(True)
        for s in ax.spines.values():
            s.set_visible(False)
        ax.set_title(title, loc="left", fontsize=12.5, fontweight="bold", color=INK, pad=18)
        ax.text(0, 1.004, sub, transform=ax.transAxes, fontsize=8.5, color=MUTED, va="bottom")
    axes[0].set_yticks(range(n), [m["name"] for m in models])
    axes[0].set_ylim(-0.7, n - 0.3)

    handles = [Line2D([], [], marker="o", ls="", ms=7, color=c, label=label) for c, label in GROUP_STYLE.values()]
    handles.append(
        Line2D([], [], marker="o", ls="", ms=7, mfc="white", mec=MUTED, mew=1.6, label="hollow: direct forces")
    )
    fig.legend(
        handles=handles,
        loc="lower center",
        ncol=4,
        frameon=False,
        fontsize=9,
        bbox_to_anchor=(0.58, 0),
        handletextpad=0.3,
    )
    h = fig.get_figheight()
    fig.text(0.012, 1 - 0.25 / h, "Foundation MLIPs on Matbench Discovery", fontsize=17, fontweight="bold", color=INK)
    fig.text(
        0.012,
        1 - 0.52 / h,
        f"{n} models with released weights, ranked by F1. Bold values: top three in each column. "
        f"Data: Matbench Discovery, commit {commit[:7]}.",
        fontsize=9.5,
        color=MUTED,
    )
    fig.subplots_adjust(left=0.17, right=0.985, top=1 - 1.45 / h, bottom=0.75 / h)
    return fig


def save_figures(models, commit):
    out = ROOT / "figures"
    out.mkdir(exist_ok=True)
    fig = fig_hero(models, commit)
    fig.savefig(out / "hero.svg", facecolor="white", metadata={"Date": None})
    plt.close(fig)


# ---------------------------------------------------------------- README


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
        models, _ = load_models(mbd)

    stars = previous if args.offline else fetch_stars(models, previous)
    families = yaml.safe_load((ROOT / "data" / "families.yaml").read_text())
    beyond = yaml.safe_load((ROOT / "data" / "beyond_pbe.yaml").read_text())

    save_figures(models, commit)
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
        "FIG_HERO": '<img src="figures/hero.svg" alt="F1, phonon error and structure RMSD of every model, ranked by F1"'
        ' width="100%">',
    }.items():
        readme = readme.replace("{{" + key + "}}", value)
    leftover = re.findall(r"\{\{[A-Z_]+\}\}", readme)
    if leftover:
        raise SystemExit(f"unfilled placeholders: {leftover}")
    (ROOT / "README.md").write_text(readme)
    print(f"{len(models)} models, {len(stars)} repos with stars, Matbench Discovery {commit[:7]}")


if __name__ == "__main__":
    main()
