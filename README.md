<!-- markdownlint-disable -->
<h1 align="center">
    Best of MLIPs
    <br>
</h1>

<p align="center">
    <strong>A ranked list of machine-learned interatomic potentials: pretrained universal models, the codes behind them, and their data and benchmarks. Updated weekly.</strong>
</p>

<p align="center">
    <a href="https://best-of.org" title="Best-of Badge"><img src="http://bit.ly/3o3EHNN"></a>
    <a href="#contents" title="Project Count"><img src="https://img.shields.io/badge/projects-80-blue.svg?color=5ac4bf"></a>
    <a href="#contribution" title="Contributions are welcome"><img src="https://img.shields.io/badge/contributions-welcome-green.svg"></a>
</p>

This list contains 80 open-source projects with a total of 20K stars. Projects are ranked by the [project-quality score](https://github.com/best-of-lists/best-of-generator#project-quality-score) of best-of-generator, computed from GitHub and package-manager metadata. To add or update a project, open an [issue](https://github.com/NabKh/best-of-mlips/issues/new/choose), submit a [pull request](https://github.com/NabKh/best-of-mlips/pulls), or edit [projects.yaml](https://github.com/NabKh/best-of-mlips/edit/main/projects.yaml) directly.

Universal potentials carry two kinds of labels: the license of the released weights, which is often not the license of the code, and the level of theory of the training data. Models trained on different functionals are not interchangeable without refitting or correction.

<strong>How to cite.</strong> See the button "Cite this repository" on the right side-bar.

## Contents

- [Universal potentials](#universal-potentials) _25 projects_
- [MLIP codes](#mlip-codes) _15 projects_
- [Simulation](#simulation) _10 projects_
- [Active learning and fine-tuning](#active-learning-and-fine-tuning) _11 projects_
- [Datasets](#datasets) _11 projects_
- [Benchmarks](#benchmarks) _8 projects_

## Explanation
- 🥇🥈🥉&nbsp; Combined project-quality score
- ⭐️&nbsp; Star count from GitHub
- 🐣&nbsp; New project _(less than 6 months old)_
- 💤&nbsp; Inactive project _(6 months no activity)_
- 💀&nbsp; Dead project _(12 months no activity)_
- 📈📉&nbsp; Project is trending up or down
- ➕&nbsp; Project was recently added
- 👨‍💻&nbsp; Contributors count from GitHub
- 🔀&nbsp; Fork count from GitHub
- 📋&nbsp; Issue count from GitHub
- ⏱️&nbsp; Last update timestamp on package manager
- 📥&nbsp; Download count from package manager
- 📦&nbsp; Number of dependent projects

<br>

## Universal potentials

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Pretrained interatomic potentials meant to be used across most of the periodic table. Labels give the license of the weights (which can differ from the code license) and the level of theory of the training data._

<details><summary><b><a href="https://github.com/deepmodeling/deepmd-kit">DeePMD-kit</a></b> (🥇30 ·  ⭐ 2.1K) - Code and the DPA-3.1 and DPA-4 models; DPA-3.1-3M has one head per training set in the OpenLAM collection. <code><a href="http://bit.ly/37RvQcA">LGPL-3.0</a></code> <code>weights: CC-BY-4.0</code> <code>weights: LGPL-3.0</code> <code>PBE(+U)</code> <code>multi-head</code></summary>

- [GitHub](https://github.com/deepmodeling/deepmd-kit) (👨‍💻 96 · 🔀 630 · 📥 79K · 📦 63 · 📋 1.2K - 13% open · ⏱️ 21.10.2026):

	```
	git clone https://github.com/deepmodeling/deepmd-kit
	```
- [PyPi](https://pypi.org/project/deepmd-kit) (📥 17K / month):
	```
	pip install deepmd-kit
	```
</details>
<details><summary><b><a href="https://github.com/facebookresearch/fairchem">fairchem</a></b> (🥇27 ·  ⭐ 2.3K) - eqV2, eSEN and UMA models trained on OMat24, OMol25, OC20 and related FAIR datasets. UMA weights are gated on Hugging.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: custom (Meta)</code> <code>PBE(+U)</code> <code>ωB97M</code> <code>multi-head</code></summary>

- [GitHub](https://github.com/facebookresearch/fairchem) (👨‍💻 74 · 🔀 510 · 📋 620 - 1% open · ⏱️ 15.10.2026):

	```
	git clone https://github.com/facebookresearch/fairchem
	```
- [PyPi](https://pypi.org/project/fairchem-core) (📥 19K / month):
	```
	pip install fairchem-core
	```
</details>
<details><summary><b><a href="https://github.com/mir-group/nequip">NequIP</a></b> (🥇27 ·  ⭐ 970) - Code and the Nequip-MP-L, -OAM-L and -OAM-XL foundation models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: CC-BY-4.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/mir-group/nequip) (👨‍💻 46 · 🔀 210 · 📦 59 · 📋 130 - 2% open · ⏱️ 31.08.2026):

	```
	git clone https://github.com/mir-group/nequip
	```
- [PyPi](https://pypi.org/project/nequip) (📥 5.6K / month):
	```
	pip install nequip
	```
</details>
<details><summary><b><a href="https://github.com/materialyzeai/matgl">MatGL</a></b> (🥇27 ·  ⭐ 580) - M3GNet, CHGNet and TensorNet models, including the MatPES PBE and r2SCAN potentials. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code>weights: not stated</code> <code>PBE(+U)</code> <code>r2SCAN</code></summary>

- [GitHub](https://github.com/materialyzeai/matgl) (👨‍💻 30 · 🔀 120 · 📦 100 · ⏱️ 21.10.2026):

	```
	git clone https://github.com/materialyzeai/matgl
	```
- [PyPi](https://pypi.org/project/matgl) (📥 29K / month):
	```
	pip install matgl
	```
</details>
<details><summary><b><a href="https://github.com/orbital-materials/orb-models">Orb</a></b> (🥈22 ·  ⭐ 620) - ORB v2 and v3 models trained on MPtrj, Alexandria and OMat24. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code> <code>weights: Apache-2.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/orbital-materials/orb-models) (👨‍💻 17 · 🔀 89 · 📦 48 · 📋 82 - 10% open · ⏱️ 26.09.2026):

	```
	git clone https://github.com/orbital-materials/orb-models
	```
- [PyPi](https://pypi.org/project/orb-models) (📥 13K / month):
	```
	pip install orb-models
	```
</details>
<details><summary><b><a href="https://github.com/microsoft/mattersim">MatterSim</a></b> (🥈22 ·  ⭐ 600) - MatterSim: A deep learning atomistic model across elements, temperatures and pressures. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/microsoft/mattersim) (👨‍💻 27 · 🔀 97 · 📥 46 · 📋 48 - 10% open · ⏱️ 21.10.2026):

	```
	git clone https://github.com/microsoft/mattersim
	```
- [PyPi](https://pypi.org/project/mattersim) (📥 24K / month):
	```
	pip install mattersim
	```
</details>
<details><summary><b><a href="https://github.com/lab-cosmo/upet">UPET</a></b> (🥈22 ·  ⭐ 240) - PET-MAD (PBEsol in v1.0, r2SCAN from v1.5) and PET-OAM-XL. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code>weights: BSD-3</code> <code>PBE(+U)</code> <code>PBEsol</code> <code>r2SCAN</code></summary>

- [GitHub](https://github.com/lab-cosmo/upet) (👨‍💻 19 · 🔀 25 · 📥 120 · 📦 15 · 📋 25 - 4% open · ⏱️ 02.10.2026):

	```
	git clone https://github.com/lab-cosmo/upet
	```
- [PyPi](https://pypi.org/project/upet) (📥 2.9K / month):
	```
	pip install upet
	```
</details>
<details><summary><b><a href="https://github.com/isayevlab/aimnetcentral">AIMNet2</a></b> (🥈22 ·  ⭐ 120) - Neutral and charged molecules, 14 elements, wB97M-D3(BJ). <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>ωB97M</code> <code>molecules</code></summary>

- [GitHub](https://github.com/isayevlab/aimnetcentral) (👨‍💻 7 · 🔀 34 · 📦 16 · 📋 27 - 18% open · ⏱️ 14.10.2026):

	```
	git clone https://github.com/isayevlab/aimnetcentral
	```
- [PyPi](https://pypi.org/project/aimnet) (📥 4.7K / month):
	```
	pip install aimnet
	```
</details>
<details><summary><b><a href="https://github.com/CederGroupHub/chgnet">CHGNet</a></b> (🥈21 ·  ⭐ 410) - Charge-informed graph network trained on MPtrj. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code>weights: BSD-3</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/CederGroupHub/chgnet) (👨‍💻 14 · 🔀 100 · 📦 83 · 📋 78 - 5% open · ⏱️ 15.09.2026):

	```
	git clone https://github.com/CederGroupHub/chgnet
	```
- [PyPi](https://pypi.org/project/chgnet) (📥 26K / month):
	```
	pip install chgnet
	```
</details>
<details><summary><b><a href="https://github.com/MDIL-SNU/SevenNet">SevenNet</a></b> (🥈21 ·  ⭐ 280) - SevenNet-l3i5 (GPL-3.0) and the multi-fidelity SevenNet-Omni (MIT). <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>weights: GPL-3.0</code> <code>PBE(+U)</code> <code>multi-head</code></summary>

- [GitHub](https://github.com/MDIL-SNU/SevenNet) (👨‍💻 22 · 🔀 57 · 📥 46K · 📋 99 - 18% open · ⏱️ 06.10.2026):

	```
	git clone https://github.com/MDIL-SNU/SevenNet
	```
- [PyPi](https://pypi.org/project/sevenn) (📥 16K / month):
	```
	pip install sevenn
	```
</details>
<details><summary><b><a href="https://github.com/mir-group/allegro">Allegro</a></b> (🥉20 ·  ⭐ 500) - Strictly local equivariant potentials; Allegro-MP-L and -OAM-L foundation models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: CC-BY-4.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/mir-group/allegro) (👨‍💻 10 · 🔀 75 · 📦 5 · 📋 51 - 1% open · ⏱️ 28.05.2026):

	```
	git clone https://github.com/mir-group/allegro
	```
- [PyPi](https://pypi.org/project/nequip-allegro) (📥 1.2K / month):
	```
	pip install nequip-allegro
	```
</details>
<details><summary><b><a href="https://github.com/ACEsuit/mace-foundations">MACE foundation models</a></b> (🥉17 ·  ⭐ 320) - MACE-MP-0 and MACE-MPA-0 (MIT); MACE-OMAT-0, MACE-MATPES-PBE-0 / -r2SCAN-0, MACE-OMOL-0 and the multi-head MACE-MH-1.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <a href="https://github.com/gabor1/ASL"><code>weights: ASL (non-commercial)</code></a> <code>PBE(+U)</code> <code>r2SCAN</code> <code>ωB97M</code> <code>multi-head</code></summary>

- [GitHub](https://github.com/ACEsuit/mace-foundations) (👨‍💻 6 · 🔀 32 · 📥 830K · 📋 45 - 22% open · ⏱️ 26.08.2026):

	```
	git clone https://github.com/ACEsuit/mace-foundations
	```
- [PyPi](https://pypi.org/project/mace-torch) (📥 76K / month):
	```
	pip install mace-torch
	```
</details>
<details><summary><b><a href="https://github.com/xvzemin/tace">TACE</a></b> (🥉17 ·  ⭐ 73) - Tensor Atomic/Edge Cluster Expansion. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: CC-BY-4.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/xvzemin/tace) (🔀 7 · ⏱️ 20.10.2026):

	```
	git clone https://github.com/xvzemin/tace
	```
- [PyPi](https://pypi.org/project/tace) (📥 280 / month):
	```
	pip install tace
	```
</details>
<details><summary><b><a href="https://github.com/ICAMS/grace-tensorpotential">GRACE</a></b> (🥉15 ·  ⭐ 110) - GRACE-1L and 2L/3L models trained on MPtrj and OMat24. <code><a href="https://github.com/ICAMS/grace-tensorpotential/blob/HEAD/LICENSE.md">Custom</a></code> <a href="https://github.com/gabor1/ASL"><code>weights: ASL (non-commercial)</code></a> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/ICAMS/grace-tensorpotential) (👨‍💻 5 · 🔀 20 · 📦 17 · 📋 21 - 66% open · ⏱️ 17.10.2026):

	```
	git clone https://github.com/ICAMS/grace-tensorpotential
	```
- [PyPi](https://pypi.org/project/tensorpotential) (📥 1.8K / month):
	```
	pip install tensorpotential
	```
</details>
<details><summary><b><a href="https://github.com/atomicarchitects/nequix">Nequix</a></b> (🥉15 ·  ⭐ 80) - [ICML26] Phonon fine-tuning (PFT) and [NeurIPS25 AI4Mat] Nequix: Training a foundation model for materials on a budget. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: CC-BY-4.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/atomicarchitects/nequix) (👨‍💻 5 · 🔀 16 · 📋 5 - 40% open · ⏱️ 02.04.2026):

	```
	git clone https://github.com/atomicarchitects/nequix
	```
- [PyPi](https://pypi.org/project/nequix) (📥 52K / month):
	```
	pip install nequix
	```
</details>
<details><summary><b><a href="https://github.com/general-molecular-simulations/so3lr">SO3LR</a></b> (🥉13 ·  ⭐ 240) - SO3krates with explicit long-range electrostatics and dispersion, trained at PBE0+MBD. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>PBE0+MBD</code> <code>molecules</code></summary>

- [GitHub](https://github.com/general-molecular-simulations/so3lr) (👨‍💻 7 · 🔀 33 · 📋 24 - 54% open · ⏱️ 17.04.2026):

	```
	git clone https://github.com/general-molecular-simulations/so3lr
	```
</details>
<details><summary><b><a href="https://github.com/HPC-AI-Team/MatRIS">MatRIS</a></b> (🥉13 ·  ⭐ 45) - This repository contains the official PyTorch implementation of MatRIS. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code>weights: BSD-3</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/HPC-AI-Team/MatRIS) (👨‍💻 4 · 🔀 7 · 📥 180 · 📋 4 - 25% open · ⏱️ 03.10.2026):

	```
	git clone https://github.com/HPC-AI-Team/MatRIS
	```
- [PyPi](https://pypi.org/project/matris) (📥 300 / month):
	```
	pip install matris
	```
</details>
<details><summary><b><a href="https://github.com/myung-group/BAM-torch">BAM</a></b> (🥉11 ·  ⭐ 6) - BAM-MP-DeNS, trained on MPtrj. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/myung-group/BAM-torch) (👨‍💻 12 · 🔀 6 · ⏱️ 20.10.2026):

	```
	git clone https://github.com/myung-group/BAM-torch
	```
</details>
<details><summary><b><a href="https://github.com/zmyybc/AlphaNet">AlphaNet</a></b> (🥉9 ·  ⭐ 120) - A Local Frame-based Atomistic Potential. <code><a href="http://bit.ly/2M0xdwT">GPL-3.0</a></code> <code>weights: GPL-3.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/zmyybc/AlphaNet) (👨‍💻 3 · 🔀 30 · 📋 6 - 16% open · ⏱️ 26.07.2026):

	```
	git clone https://github.com/zmyybc/AlphaNet
	```
</details>
<details><summary><b><a href="https://github.com/rowansci/egret-public">Egret-1</a></b> (🥉8 ·  ⭐ 81 · 💤) - Bioorganic and main-group molecules, wB97M-D3(BJ)/def2-TZVPPD. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>ωB97M</code> <code>molecules</code></summary>

- [GitHub](https://github.com/rowansci/egret-public) (👨‍💻 3 · 🔀 7 · ⏱️ 15.12.2025):

	```
	git clone https://github.com/rowansci/egret-public
	```
</details>
<details><summary><b><a href="https://github.com/atomicarchitects/equiformer_v3">EquiformerV3</a></b> (🥉6 ·  ⭐ 130 · 🐣) - EquiformerV3: Scaling Efficient, Expressive, and General SE(3)-Equivariant Graph Attention Transformers. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/atomicarchitects/equiformer_v3) (🔀 21 · 📋 6 - 66% open · ⏱️ 17.04.2026):

	```
	git clone https://github.com/atomicarchitects/equiformer_v3
	```
</details>
<details><summary><b><a href="https://github.com/kairosmaterial/prophet">Prophet</a></b> (🥉6 ·  ⭐ 57 · 🐣) - Atomistic foundation models for materials simulation and discovery. Research previews from Kairos Materials. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: CC-BY-4.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/kairosmaterial/prophet) (🔀 2 · ⏱️ 02.10.2026):

	```
	git clone https://github.com/kairosmaterial/prophet
	```
</details>
<details><summary><b><a href="https://github.com/SamsungDS/GGNN">EquFlash</a></b> (🥉3 ·  ⭐ 21 · 🐣) - EquFlash and EquFlashV2. The repository LICENSE.md is CC BY-NC-SA 4.0. <code><a href="https://tldrlegal.com/search?q=CC-BY-NC-SA-4.0">CC-BY-NC-SA-4.0</a></code> <code>weights: CC-BY-NC-SA-4.0</code> <code>PBE(+U)</code></summary>

- [GitHub](https://github.com/SamsungDS/GGNN) (👨‍💻 2 · 🔀 3 · 📋 2 - 50% open · ⏱️ 03.07.2026):

	```
	git clone https://github.com/SamsungDS/GGNN
	```
</details>
<details><summary>Show 2 hidden projects...</summary>

- <b><a href="https://github.com/yzchen08/eqnorm">Eqnorm</a></b> (🥉6 ·  ⭐ 14 · 💀) - generalized machine learning potential eqnorm. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>weights: MIT</code> <code>PBE(+U)</code>
- <b><a href="https://github.com/ACEsuit/mace-off">MACE-OFF</a></b> (🥉5 ·  ⭐ 77 · 💀) - MACE-OFF23 and OFF24 for neutral organic molecules, trained on SPICE at wB97M-D3(BJ)/def2-TZVPPD. <code><a href="https://github.com/ACEsuit/mace-off/blob/HEAD/LICENSE.md">Custom</a></code> <a href="https://github.com/gabor1/ASL"><code>weights: ASL (non-commercial)</code></a> <code>ωB97M</code> <code>molecules</code>
</details>
<br>

## MLIP codes

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Codes for building and training machine-learned interatomic potentials._

<details><summary><b><a href="https://github.com/ACEsuit/mace">MACE</a></b> (🥇29 ·  ⭐ 1.4K) - MACE - Fast and accurate machine learning interatomic potentials with higher order equivariant message passing. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/ACEsuit/mace) (👨‍💻 83 · 🔀 480 · 📋 690 - 28% open · ⏱️ 15.10.2026):

	```
	git clone https://github.com/ACEsuit/mace
	```
- [PyPi](https://pypi.org/project/mace-torch) (📥 76K / month):
	```
	pip install mace-torch
	```
</details>
<details><summary><b><a href="https://github.com/aiqm/torchani">TorchANI</a></b> (🥇25 ·  ⭐ 560) - TorchANI 2.0 is an open-source library that supports training, development, and research of ANI-style neural network.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/aiqm/torchani) (👨‍💻 19 · 🔀 140 · 📦 87 · 📋 180 - 1% open · ⏱️ 06.09.2026):

	```
	git clone https://github.com/aiqm/torchani
	```
- [PyPi](https://pypi.org/project/torchani) (📥 4.5K / month):
	```
	pip install torchani
	```
</details>
<details><summary><b><a href="https://github.com/metatensor/metatrain">metatrain</a></b> (🥈24 ·  ⭐ 82) - Train, fine-tune, and manipulate machine learning models for atomistic systems. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/metatensor/metatrain) (👨‍💻 38 · 🔀 39 · 📥 120 · 📦 19 · 📋 310 - 25% open · ⏱️ 21.10.2026):

	```
	git clone https://github.com/metatensor/metatrain
	```
- [PyPi](https://pypi.org/project/metatrain) (📥 4.3K / month):
	```
	pip install metatrain
	```
</details>
<details><summary><b><a href="https://github.com/torchmd/torchmd-net">TorchMD-NET</a></b> (🥈18 ·  ⭐ 480) - Training neural network potentials. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/torchmd/torchmd-net) (👨‍💻 20 · 🔀 96 · 📥 240 · 📋 120 - 26% open · ⏱️ 19.10.2026):

	```
	git clone https://github.com/torchmd/torchmd-net
	```
- [PyPi](https://pypi.org/project/torchmd-net) (📥 610 / month):
	```
	pip install torchmd-net
	```
</details>
<details><summary><b><a href="https://github.com/vldgroup/graph-pes">graph-pes</a></b> (🥈16 ·  ⭐ 130) - train and use graph-based ML models of potential energy surfaces. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/vldgroup/graph-pes) (👨‍💻 8 · 🔀 16 · 📦 3 · 📋 20 - 30% open · ⏱️ 22.09.2026):

	```
	git clone https://github.com/vldgroup/graph-pes
	```
- [PyPi](https://pypi.org/project/graph-pes) (📥 1.1K / month):
	```
	pip install graph-pes
	```
</details>
<details><summary><b><a href="https://github.com/ICAMS/python-ace">pacemaker</a></b> (🥈16 ·  ⭐ 120) - Fitting of atomic cluster expansion (ACE) potentials. <code><a href="https://github.com/ICAMS/python-ace/blob/HEAD/LICENSE.md">Custom</a></code></summary>

- [GitHub](https://github.com/ICAMS/python-ace) (👨‍💻 9 · 🔀 27 · 📋 70 - 41% open · ⏱️ 04.09.2026):

	```
	git clone https://github.com/ICAMS/python-ace
	```
- [PyPi](https://pypi.org/project/python-ace) (📥 210 / month):
	```
	pip install python-ace
	```
</details>
<details><summary><b><a href="https://github.com/openkim/kliff">KLIFF</a></b> (🥈16 ·  ⭐ 40 · 💤) - KIM-based Learning-Integrated Fitting Framework for interatomic potentials. <code><a href="https://tldrlegal.com/search?q=LGPL-2.1">LGPL-2.1</a></code></summary>

- [GitHub](https://github.com/openkim/kliff) (👨‍💻 14 · 🔀 21 · 📦 4 · 📋 51 - 35% open · ⏱️ 28.02.2026):

	```
	git clone https://github.com/openkim/kliff
	```
- [PyPi](https://pypi.org/project/kliff) (📥 82 / month):
	```
	pip install kliff
	```
</details>
<details><summary><b><a href="https://github.com/apax-hub/apax">apax</a></b> (🥈16 ·  ⭐ 38) - A flexible and performant framework for training machine learning potentials. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/apax-hub/apax) (👨‍💻 11 · 🔀 8 · 📦 7 · 📋 180 - 15% open · ⏱️ 01.06.2026):

	```
	git clone https://github.com/apax-hub/apax
	```
- [PyPi](https://pypi.org/project/apax) (📥 130 / month):
	```
	pip install apax
	```
</details>
<details><summary><b><a href="https://github.com/Teoroo-CMC/PiNN">PiNN</a></b> (🥉15 ·  ⭐ 130) - A Python library for building atomic neural networks. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/Teoroo-CMC/PiNN) (👨‍💻 9 · 🔀 41 · ⏱️ 17.09.2026):

	```
	git clone https://github.com/Teoroo-CMC/PiNN
	```
</details>
<details><summary><b><a href="https://github.com/libAtoms/GAP">GAP</a></b> (🥉9 ·  ⭐ 49) - Gaussian approximation potentials. <code><a href="https://github.com/libAtoms/GAP/blob/HEAD/LICENSE.md">Custom</a></code></summary>

- [GitHub](https://github.com/libAtoms/GAP) (👨‍💻 13 · 🔀 21 · ⏱️ 05.07.2026):

	```
	git clone https://github.com/libAtoms/GAP
	```
</details>
<details><summary><b><a href="https://gitlab.com/ashapeev/mlip-3">MLIP-3</a></b> (🥉3) - Moment tensor potentials. <code><a href="http://bit.ly/3rqEWVr">BSD-2</a></code></summary>

- _No project information available._</details>
<details><summary><b><a href="https://gitlab.com/PANNAdevs/panna">PANNA</a></b> (🥉3) - Properties from artificial neural network architectures. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- _No project information available._</details>
<details><summary>Show 3 hidden projects...</summary>

- <b><a href="https://github.com/uf3/uf3">UF3</a></b> (🥈16 ·  ⭐ 74 · 💀) - UF3: a python library for generating ultra-fast interatomic potentials. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code>
- <b><a href="https://github.com/CompPhysVienna/n2p2">n2p2</a></b> (🥉13 ·  ⭐ 240 · 💀) - n2p2 - A Neural Network Potential Package. <code><a href="http://bit.ly/2M0xdwT">GPL-3.0</a></code>
- <b><a href="https://github.com/MaterSim/PyXtal_FF">PyXtal_FF</a></b> (🥉11 ·  ⭐ 93 · 💀) - Machine Learning Interatomic Potential Predictions. <code>Unlicensed</code>
</details>
<br>

## Simulation

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_MD engines, plugins and calculators that run machine-learned potentials._

<details><summary><b><a href="https://github.com/jax-md/jax-md">JAX MD</a></b> (🥇26 ·  ⭐ 1.5K) - Differentiable, Hardware Accelerated, Molecular Dynamics. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code></summary>

- [GitHub](https://github.com/jax-md/jax-md) (👨‍💻 54 · 🔀 250 · 📦 100 · 📋 180 - 20% open · ⏱️ 18.08.2026):

	```
	git clone https://github.com/jax-md/jax-md
	```
- [PyPi](https://pypi.org/project/jax-md) (📥 23K / month):
	```
	pip install jax-md
	```
</details>
<details><summary><b><a href="https://github.com/materialyzeai/matcalc">MatCalc</a></b> (🥈25 ·  ⭐ 160) - A python library for calculating materials properties from the PES. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/materialyzeai/matcalc) (👨‍💻 24 · 🔀 38 · 📦 27 · 📋 45 - 2% open · ⏱️ 08.10.2026):

	```
	git clone https://github.com/materialyzeai/matcalc
	```
- [PyPi](https://pypi.org/project/matcalc) (📥 9.7K / month):
	```
	pip install matcalc
	```
</details>
<details><summary><b><a href="https://github.com/brucefan1983/GPUMD">GPUMD</a></b> (🥈23 ·  ⭐ 860) - Graphics Processing Units Molecular Dynamics. <code><a href="https://github.com/brucefan1983/GPUMD/blob/HEAD/LICENSES">Custom</a></code></summary>

- [GitHub](https://github.com/brucefan1983/GPUMD) (👨‍💻 70 · 🔀 210 · 📋 290 - 4% open · ⏱️ 21.10.2026):

	```
	git clone https://github.com/brucefan1983/GPUMD
	```
</details>
<details><summary><b><a href="https://github.com/TorchSim/torch-sim">TorchSim</a></b> (🥈23 ·  ⭐ 500) - Torch-native, batchable, atomistic simulations. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/TorchSim/torch-sim) (👨‍💻 39 · 🔀 110 · 📋 180 - 10% open · ⏱️ 18.10.2026):

	```
	git clone https://github.com/TorchSim/torch-sim
	```
- [PyPi](https://pypi.org/project/torch-sim-atomistic) (📥 23K / month):
	```
	pip install torch-sim-atomistic
	```
</details>
<details><summary><b><a href="https://github.com/stfc/janus-core">janus-core</a></b> (🥉21 ·  ⭐ 51) - Tools for machine learnt interatomic potentials. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/stfc/janus-core) (👨‍💻 11 · 🔀 18 · 📥 280 · 📦 19 · 📋 310 - 15% open · ⏱️ 02.10.2026):

	```
	git clone https://github.com/stfc/janus-core
	```
- [PyPi](https://pypi.org/project/janus-core) (📥 4K / month):
	```
	pip install janus-core
	```
</details>
<details><summary><b><a href="https://github.com/openmm/openmm-ml">OpenMM-ML</a></b> (🥉15 ·  ⭐ 180) - High level API for using machine learning models in OpenMM simulations. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/openmm/openmm-ml) (👨‍💻 12 · 🔀 44 · 📦 2 · 📋 85 - 31% open · ⏱️ 20.10.2026):

	```
	git clone https://github.com/openmm/openmm-ml
	```
</details>
<details><summary><b><a href="https://github.com/mir-group/pair_nequip_allegro">pair_nequip_allegro</a></b> (🥉13 ·  ⭐ 65) - LAMMPS pair styles for NequIP and Allegro. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/mir-group/pair_nequip_allegro) (👨‍💻 6 · 🔀 12 · 📋 52 - 23% open · ⏱️ 14.05.2026):

	```
	git clone https://github.com/mir-group/pair_nequip_allegro
	```
</details>
<details><summary><b><a href="https://github.com/molmod/psiflow">psiflow</a></b> (🥉12 ·  ⭐ 140) - scalable molecular simulation. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/molmod/psiflow) (👨‍💻 5 · 🔀 15 · 📋 60 - 18% open · ⏱️ 28.04.2026):

	```
	git clone https://github.com/molmod/psiflow
	```
</details>
<details><summary><b><a href="https://github.com/openmm/openmm-torch">OpenMM Torch</a></b> (🥉11 ·  ⭐ 220) - OpenMM plugin to define forces with neural networks. <code>Unlicensed</code></summary>

- [GitHub](https://github.com/openmm/openmm-torch) (👨‍💻 9 · 🔀 33 · 📋 110 - 33% open · ⏱️ 24.06.2026):

	```
	git clone https://github.com/openmm/openmm-torch
	```
</details>
<details><summary><b><a href="https://github.com/ICAMS/lammps-user-pace">lammps-user-pace</a></b> (🥉8 ·  ⭐ 34 · 💤) - LAMMPS pair style for ACE and GRACE potentials. <code><a href="http://bit.ly/2KucAZR">GPL-2.0</a></code></summary>

- [GitHub](https://github.com/ICAMS/lammps-user-pace) (👨‍💻 8 · 🔀 17 · 📋 9 - 33% open · ⏱️ 03.12.2025):

	```
	git clone https://github.com/ICAMS/lammps-user-pace
	```
</details>
<br>

## Active learning and fine-tuning

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Workflows that generate training data, fit or fine-tune potentials iteratively._

<details><summary><b><a href="https://github.com/deepmodeling/dpgen">DP-GEN</a></b> (🥇24 ·  ⭐ 400) - The deep potential generator to generate a deep-learning based model of interatomic potential energy and force field. <code><a href="http://bit.ly/37RvQcA">LGPL-3.0</a></code></summary>

- [GitHub](https://github.com/deepmodeling/dpgen) (👨‍💻 76 · 🔀 190 · 📥 2.1K · 📦 8 · 📋 370 - 2% open · ⏱️ 15.09.2026):

	```
	git clone https://github.com/deepmodeling/dpgen
	```
- [PyPi](https://pypi.org/project/dpgen) (📥 510 / month):
	```
	pip install dpgen
	```
</details>
<details><summary><b><a href="https://github.com/mir-group/flare">FLARE</a></b> (🥇22 ·  ⭐ 360) - An open-source Python package for creating fast and accurate interatomic potentials. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/mir-group/flare) (👨‍💻 44 · 🔀 77 · 📥 10 · 📦 12 · 📋 220 - 8% open · ⏱️ 19.09.2026):

	```
	git clone https://github.com/mir-group/flare
	```
- [PyPi](https://pypi.org/project/mir-flare) (📥 320 / month):
	```
	pip install mir-flare
	```
</details>
<details><summary><b><a href="https://github.com/autoatml/autoplex">autoplex</a></b> (🥈18 ·  ⭐ 160) - Code for automated fitting of machine learned interatomic potentials. <code><a href="http://bit.ly/2M0xdwT">GPL-3.0</a></code></summary>

- [GitHub](https://github.com/autoatml/autoplex) (👨‍💻 18 · 🔀 28 · 📦 2 · 📋 150 - 22% open · ⏱️ 21.10.2026):

	```
	git clone https://github.com/autoatml/autoplex
	```
- [PyPi](https://pypi.org/project/autoplex) (📥 100 / month):
	```
	pip install autoplex
	```
</details>
<details><summary><b><a href="https://github.com/deepmodeling/dpgen2">DP-GEN2</a></b> (🥈18 ·  ⭐ 43) - 2nd generation of the Deep Potential GENerator. <code><a href="http://bit.ly/37RvQcA">LGPL-3.0</a></code></summary>

- [GitHub](https://github.com/deepmodeling/dpgen2) (👨‍💻 21 · 🔀 36 · 📦 6 · 📋 66 - 48% open · ⏱️ 07.09.2026):

	```
	git clone https://github.com/deepmodeling/dpgen2
	```
- [PyPi](https://pypi.org/project/dpgen2) (📥 57 / month):
	```
	pip install dpgen2
	```
</details>
<details><summary><b><a href="https://github.com/libAtoms/workflow">wfl</a></b> (🥈16 ·  ⭐ 42) - python workflow toolkit. <code><a href="http://bit.ly/2KucAZR">GPL-2.0</a></code></summary>

- [GitHub](https://github.com/libAtoms/workflow) (👨‍💻 21 · 🔀 21 · 📦 6 · 📋 170 - 40% open · ⏱️ 22.07.2026):

	```
	git clone https://github.com/libAtoms/workflow
	```
</details>
<details><summary><b><a href="https://github.com/stfc/aiida-mlip">aiida-mlip</a></b> (🥈16 ·  ⭐ 26) - machine learning interatomic potentials aiida plugin. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code></summary>

- [GitHub](https://github.com/stfc/aiida-mlip) (👨‍💻 10 · 🔀 14 · 📥 60 · 📦 4 · 📋 160 - 40% open · ⏱️ 02.10.2026):

	```
	git clone https://github.com/stfc/aiida-mlip
	```
- [PyPi](https://pypi.org/project/aiida-mlip) (📥 340 / month):
	```
	pip install aiida-mlip
	```
</details>
<details><summary><b><a href="https://github.com/zincware/IPSuite">IPSuite</a></b> (🥈16 ·  ⭐ 25 · 💤) - Machine Learned Interatomic Potential Tools. <code><a href="http://bit.ly/2M0xmjV">EPL-2.0</a></code></summary>

- [GitHub](https://github.com/zincware/IPSuite) (👨‍💻 9 · 🔀 13 · 📦 14 · 📋 160 - 42% open · ⏱️ 13.03.2026):

	```
	git clone https://github.com/zincware/IPSuite
	```
- [PyPi](https://pypi.org/project/ipsuite) (📥 300 / month):
	```
	pip install ipsuite
	```
</details>
<details><summary><b><a href="https://github.com/FitSNAP/FitSNAP">FitSNAP</a></b> (🥉14 ·  ⭐ 190 · 💤) - Software for generating machine-learning interatomic potentials for LAMMPS. <code><a href="http://bit.ly/2KucAZR">GPL-2.0</a></code></summary>

- [GitHub](https://github.com/FitSNAP/FitSNAP) (👨‍💻 23 · 🔀 64 · 📥 19 · 📋 75 - 16% open · ⏱️ 17.10.2025):

	```
	git clone https://github.com/FitSNAP/FitSNAP
	```
</details>
<details><summary>Show 3 hidden projects...</summary>

- <b><a href="https://github.com/ulissigroup/finetuna">FINETUNA</a></b> (🥉9 ·  ⭐ 71 · 💀) - Active Learning for Machine Learning Potentials. <code><a href="http://bit.ly/34MBwT8">MIT</a></code>
- <b><a href="https://github.com/ACEsuit/ACEHAL">ACEHAL</a></b> (🥉5 ·  ⭐ 16 · 💀) - Hyperactive learning (HAL) for building ACE potentials. <code>Unlicensed</code>
- <b><a href="https://github.com/nec-research/alebrew">ALEBREW</a></b> (🥉4 ·  ⭐ 21 · 💀) - Official repository for the paper Uncertainty-biased molecular dynamics for learning uniformly accurate interatomic.. <code><a href="https://github.com/nec-research/alebrew/blob/HEAD/LICENSE.txt">Custom</a></code>
</details>
<br>

## Datasets

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Training data used by the potentials above._

<details><summary><b><a href="https://github.com/jla-gardner/load-atoms">load-atoms</a></b> (🥇14 ·  ⭐ 49 · 💤) - download and manipulate atomistic datasets. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/jla-gardner/load-atoms) (👨‍💻 5 · 🔀 5 · 📦 8 · 📋 34 - 11% open · ⏱️ 25.11.2025):

	```
	git clone https://github.com/jla-gardner/load-atoms
	```
- [PyPi](https://pypi.org/project/load-atoms) (📥 710 / month):
	```
	pip install load-atoms
	```
</details>
<details><summary><b><a href="https://github.com/AIRI-Institute/nablaDFT">nablaDFT</a></b> (🥈12 ·  ⭐ 240 · 💤) - nablaDFT: Large-Scale Conformational Energy and Hamiltonian Prediction benchmark and dataset. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>molecules</code></summary>

- [GitHub](https://github.com/AIRI-Institute/nablaDFT) (👨‍💻 9 · 🔀 25 · 📋 28 - 10% open · ⏱️ 31.12.2025):

	```
	git clone https://github.com/AIRI-Institute/nablaDFT
	```
</details>
<details><summary><b><a href="https://github.com/openmm/spice-dataset">SPICE</a></b> (🥈12 ·  ⭐ 210 · 💤) - A collection of QM data for training potential functions. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>ωB97M</code> <code>molecules</code></summary>

- [GitHub](https://github.com/openmm/spice-dataset) (🔀 11 · 📥 450 · 📋 74 - 25% open · ⏱️ 25.02.2026):

	```
	git clone https://github.com/openmm/spice-dataset
	```
</details>
<details><summary><b><a href="https://github.com/materialyzeai/matpes">MatPES</a></b> (🥈11 ·  ⭐ 61) - A foundational potential energy dataset for materials. <code><a href="http://bit.ly/3aKzpTv">BSD-3</a></code> <code>PBE(+U)</code> <code>r2SCAN</code></summary>

- [GitHub](https://github.com/materialyzeai/matpes) (👨‍💻 3 · 🔀 5 · ⏱️ 01.07.2026):

	```
	git clone https://github.com/materialyzeai/matpes
	```
</details>
<details><summary><b><a href="https://figshare.com/articles/dataset/Materials_Project_Trjectory_MPtrj_Dataset/23713842">MPtrj</a></b> (🥉3) - PBE/PBE+U relaxation trajectories from the Materials Project, released with CHGNet. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>PBE(+U)</code></summary>

- _No project information available._</details>
<details><summary><b><a href="https://figshare.com/articles/dataset/MPF_2021_2_8/19470599">MPF.2021.2.8</a></b> (🥉2) - Materials Project relaxation trajectories used to train M3GNet. <code><a href="https://tldrlegal.com/search?q=CC-BY-4.0">CC-BY-4.0</a></code> <code>PBE(+U)</code></summary>

- _No project information available._</details>
<details><summary><b><a href="https://huggingface.co/datasets/facebook/OMAT24">OMat24</a></b> (🥉2) - Non-equilibrium bulk structures computed with PBE(+U), from FAIR Chemistry. <code><a href="https://tldrlegal.com/search?q=CC-BY-4.0">CC-BY-4.0</a></code> <code>PBE(+U)</code></summary>

- _No project information available._</details>
<details><summary><b><a href="https://huggingface.co/facebook/OMol25">OMol25</a></b> (🥉2) - Molecular dataset at wB97M-V/def2-TZVPD, from FAIR Chemistry. <code><a href="https://huggingface.co/facebook/OMol25">Custom</a></code> <code>ωB97M</code> <code>molecules</code></summary>

- _No project information available._</details>
<details><summary><b><a href="https://alexandria.icams.rub.de/">Alexandria</a></b> (🥉1) - Database of DFT calculations for periodic materials. sAlex, a subset, is used in many universal potentials. <code>Unlicensed</code> <code>PBE(+U)</code></summary>

- _No project information available._</details>
<details><summary>Show 2 hidden projects...</summary>

- <b><a href="https://github.com/valence-labs/OpenQDC">OpenQDC</a></b> (🥇13 ·  ⭐ 69 · 💀) - Repository of Quantum Datasets Publicly Available. <code><a href="https://tldrlegal.com/search?q=CC-BY-NC-4.0">CC-BY-NC-4.0</a></code> <code>molecules</code>
- <b><a href="https://github.com/aiqm/ANI1x_datasets">ANI-1x / ANI-1ccx</a></b> (🥉6 ·  ⭐ 71 · 💀) - The ANI-1ccx and ANI-1x data sets, coupled-cluster and density functional theory properties for organic molecules. <code><a href="http://bit.ly/34MBwT8">MIT</a></code> <code>molecules</code>
</details>
<br>

## Benchmarks

<a href="#contents"><img align="right" width="15" height="15" src="https://git.io/JtehR" alt="Back to top"></a>

_Leaderboards and test suites for machine-learned potentials._

<details><summary><b><a href="https://matbench-discovery.materialsproject.org">Matbench Discovery</a></b> (🥇21 ·  ⭐ 260) - An evaluation framework for machine learning models simulating high-throughput materials discovery. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/janosh/matbench-discovery) (👨‍💻 36 · 🔀 72 · 📥 2.3K · 📦 8 · ⏱️ 19.10.2026):

	```
	git clone https://github.com/janosh/matbench-discovery
	```
- [PyPi](https://pypi.org/project/matbench-discovery) (📥 1.9K / month):
	```
	pip install matbench-discovery
	```
</details>
<details><summary><b><a href="https://github.com/ddmms/ml-peg">ML-PEG</a></b> (🥈18 ·  ⭐ 71) - ML Performance and Extrapolation Guide (reference deployment https://ml-peg.stfc.ac.uk). <code><a href="http://bit.ly/2M0xdwT">GPL-3.0</a></code></summary>

- [GitHub](https://github.com/ddmms/ml-peg) (👨‍💻 43 · 🔀 72 · 📥 68 · 📋 340 - 45% open · ⏱️ 21.10.2026):

	```
	git clone https://github.com/ddmms/ml-peg
	```
- [PyPi](https://pypi.org/project/ml-peg) (📥 140 / month):
	```
	pip install ml-peg
	```
</details>
<details><summary><b><a href="https://github.com/basf/mlipx">mlipx</a></b> (🥈14 ·  ⭐ 110 · 💤) - Machine-Learned Interatomic Potential eXploration (mlipx) is designed at BASF for evaluating machine-learned.. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/basf/mlipx) (👨‍💻 5 · 🔀 8 · 📦 7 · 📋 14 - 14% open · ⏱️ 16.10.2025):

	```
	git clone https://github.com/basf/mlipx
	```
- [PyPi](https://pypi.org/project/mlipx) (📥 2.4K / month):
	```
	pip install mlipx
	```
</details>
<details><summary><b><a href="https://github.com/deepmodeling/LAMBench">LAMBench</a></b> (🥉13 ·  ⭐ 20) - A benchmark for Large Atomistic Models. <code><a href="http://bit.ly/34MBwT8">MIT</a></code></summary>

- [GitHub](https://github.com/deepmodeling/LAMBench) (👨‍💻 5 · 🔀 11 · 📋 140 - 7% open · ⏱️ 30.09.2026):

	```
	git clone https://github.com/deepmodeling/LAMBench
	```
</details>
<details><summary><b><a href="https://github.com/atomind-ai/mlip-arena">MLIP Arena</a></b> (🥉12 ·  ⭐ 110) - [NeurIPS 25 Spotlight] Fair and transparent benchmark of machine learning interatomic potentials (MLIPs), beyond basic.. <code><a href="http://bit.ly/3nYMfla">Apache-2</a></code></summary>

- [GitHub](https://github.com/atomind-ai/mlip-arena) (👨‍💻 3 · 🔀 10 · 📦 2 · 📋 20 - 50% open · ⏱️ 16.06.2026):

	```
	git clone https://github.com/atomind-ai/mlip-arena
	```
- [PyPi](https://pypi.org/project/mlip-arena) (📥 77 / month):
	```
	pip install mlip-arena
	```
</details>
<details><summary>Show 3 hidden projects...</summary>

- <b><a href="https://github.com/usnistgov/jarvis_leaderboard">JARVIS-Leaderboard</a></b> (🥉10 ·  ⭐ 76 · 💀) - A large scale benchmark of materials design methods: https://www.nature.com/articles/s41524-024-01259-w. <code><a href="https://github.com/usnistgov/jarvis_leaderboard/blob/HEAD/LICENSE.rst">Custom</a></code>
- <b><a href="https://github.com/usnistgov/chipsff">CHIPS-FF</a></b> (🥉6 ·  ⭐ 14 · 💀) - Evaluation of universal machine learning force-fields https://doi.org/10.1021/acsmaterialslett.5c00093. <code><a href="https://github.com/usnistgov/chipsff/blob/HEAD/LICENSE.rst">Custom</a></code>
- <b><a href="https://github.com/janosh/ffonons">ffonons</a></b> (🥉3 ·  ⭐ 24 · 💀) - Phonons from ML force fields. <code>Unlicensed</code>
</details>

---

## Contribution

Contributions are welcome. To add or update a project, either:

- open an issue from the [issue page](https://github.com/NabKh/best-of-mlips/issues/new/choose) and fill in the requested information, or
- edit [projects.yaml](https://github.com/NabKh/best-of-mlips/blob/main/projects.yaml) and submit a pull request. This can be done directly in the [GitHub UI](https://github.com/NabKh/best-of-mlips/edit/main/projects.yaml).

For weight licenses, link the file or model card that states the license. See the [contribution guidelines](https://github.com/NabKh/best-of-mlips/blob/main/CONTRIBUTING.md) for details.

The list is built with [best-of-generator](https://github.com/best-of-lists/best-of-generator). Many entries were first collected in [best-of-atomistic-machine-learning](https://github.com/JuDFTteam/best-of-atomistic-machine-learning); weight licenses and checkpoint names for universal potentials were cross-checked against [Matbench Discovery](https://github.com/janosh/matbench-discovery) and the model repositories.

## License

[![CC BY-SA 4.0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/by-sa.svg)](https://creativecommons.org/licenses/by-sa/4.0/)
