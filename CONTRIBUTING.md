# Contributing

Corrections and additions are welcome. Every fact on the page needs a source that a reader can open.

- **Benchmark scores, model metadata, training sets.** These come from [Matbench Discovery](https://github.com/janosh/matbench-discovery). Submit new models or fixes there; this page picks them up at the next weekly rebuild.
- **Loading snippets** live in [`data/families.yaml`](data/families.yaml). Copy the snippet from the model's README or documentation and link that page in `source`. Snippets reconstructed from memory are not accepted.
- **Models outside the benchmark** live in [`data/beyond_pbe.yaml`](data/beyond_pbe.yaml). Link the paper and the license file.
- **License corrections** go in [`data/license_overrides.yaml`](data/license_overrides.yaml), with a link to the license file in the model's own repository.

Do not edit `README.md`, `data/models.json` or `figures/`: they are generated. To rebuild locally:

```bash
pip install -r requirements.txt
python scripts/build.py              # clones Matbench Discovery and queries GitHub stars
python scripts/build.py --offline    # keeps the star counts already in data/models.json
```
