# Contributing

Contributions are welcome. The `README.md` is generated from [`projects.yaml`](projects.yaml) by [best-of-generator](https://github.com/best-of-lists/best-of-generator), so do not edit it directly.

## Add or update a project

- Open an issue with the [suggest](https://github.com/NabKh/best-of-mlips/issues/new?template=01_suggest-project.md) or [update](https://github.com/NabKh/best-of-mlips/issues/new?template=02_update-project.md) template, or
- edit `projects.yaml` and open a pull request. One project per pull request, please.

A project entry looks like this:

```yaml
  - name: "CHGNet"
    github_id: "CederGroupHub/chgnet"
    category: "uip"
    pypi_id: "chgnet"
    description: "Charge-informed graph network trained on MPtrj."
    labels: ["w-bsd", "pbe"]
```

`description` is optional; without it the GitHub description is used. The categories and labels are defined at the top of `projects.yaml`.

## Universal potentials

Entries in the `uip` category need two kinds of label:

- the license of the released weights (`w-...`). Link the license file or model card in the pull request. Weights are often licensed differently from the code.
- the level of theory of the training data (`pbe`, `r2scan`, `pbesol`, `wb97m`, `pbe0-mbd`, `multi-head`).
