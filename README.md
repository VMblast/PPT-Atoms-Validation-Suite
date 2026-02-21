# PPT-Atoms-Validation-Suite
CoFilename	Physical Validation	PPT Driver
proton_radius.py	Proton Radius Puzzle	Hydrostatic Compression
he4_binding.py	Helium-4 Binding Energy	Tetrahedral Packing
c12_cluster.py	Carbon-12 Stability	Fractal Alpha-Clustering
u235_fission.py	Fission Yield	Fluid Cavitation / Decompression
h2o_geometry.py	Water Bond Angle	Pressure Equilibrium
ionization_baselines.py	H, He, Li Ionization	Sub-atomic Node Displacement
symmetry_breaks_p2.py	Period 2 Ionization (Li-Ne)	Structural Locks / Symmetry Breaks
shell_damping_p3.py	Period 3 Ionization (Na-Ar)	Expanded Shell Damping
spectral_harmonics.py	Lyman & Balmer Series	Delta-Pressure Harmonic
harmonic_radii.py	Atomic Shell Radii	Harmonic Linear Scaling
shell_saturation.py	2n2 Capacity Rule	Surface Area Geometric Limits
decompression_rate.py	Radioactive Half-Life	Mechanical Decompression Rate
geometric_cleavage.py	Radioactive Decay Patterns	Anisotropic Geometric Cleavage
sheath_merging.py	Covalent & Ionic Bonding	Sheath Fusion Mechanics
noble_integrity.py	Octet Rule Stability	Perfectly Symmetric Saturation
zpinch_matter.py	Matter Inception (Solid Phase)mputational Verification of the Plasma Pressure Theory (PPT) Model


This repository contains a suite of 20 deterministic Python simulations used to validate the PPT-Atoms framework. Unlike standard quantum modeling which relies on probabilistic wave functions, these scripts utilize Hydrostatic Displacement Solvers and Harmonic Resonance Algorithms to calculate physical constants across sub-atomic, atomic, and molecular scales.
🔬 Scientific Context

The Plasma Pressure Theory (PPT) reinterprets the atom as a fractal displacement volume pinned by a high-density universal medium (Pinning Force, Cp​). This suite serves as the empirical backbone for the theory, demonstrating that physical constants—such as the Proton Radius and Nuclear Binding Energies—emerge naturally from fluid-dynamic equilibrium rather than abstract mathematical "fudge factors."
🛠️ Simulation Suite Overview

The suite is organized into four primary validation tiers:
1. Sub-Atomic & Nuclear Scale

    Proton_Radius_Solver.py: Resolves the "Proton Radius Puzzle" by modeling orbiter mass as displacement volume.

    Alpha_Cluster_Binding.py: Calculates the binding energy of 4He and 12C through tetrahedral geometric overlap.

    Neutron_Node_Density.py: Simulates core phase transitions and the emergence of neutral pressure nodes.

2. Atomic & Spectral Scale

    Shell_Capacity_2n2.py: Derives the 2n2 rule via harmonic surface area saturation.

    Lyman_Balmer_Transitions.py: Models the "snap-back" energy of pressure nodes between shell gradients.

    Ionization_Work_Formula.py: Calculates ionization energy as mechanical work (W=PΔV).

3. Molecular & Chemical Scale

    H2O_Bond_Equilibrium.py: Predicts the 104.5∘ water bond angle via overlap repulsion.

    Sheath_Fusion_Covalent.py: Simulates the merging of plasma double layers (DLs) in covalent bonding.

4. Macroscopic & High-Energy Scale

    Fission_Yield_Cavitation.py: Models the 235U fission yield as macroscopic medium decompression.

    Z_Pinch_Solidity_Forge.py: Simulates the compression of plasma filaments into solid lattice structures.

🚀 Getting Started
Prerequisites

    Python 3.8+

    NumPy

    Matplotlib (for visualization scripts)

Execution

Each script is standalone. To verify the Proton Radius calculation, run:
Bash

python Proton_Radius_Solver.py

📊 Results Summary
Physical Phenomenon	PPT Prediction	Accuracy
Proton Radius	0.8427 fm	> 99.8%
12C Binding Energy	92.16 MeV	100.0%
H$_2$O Bond Angle	104.5°	100.0%
Spectral Transitions	Exact	100.0%
📜 Citation

If you use these simulations or this data in your research, please cite:

    Milošević, V. (2026). Comprehensive Computational Validation of PPT-Atoms: Hydrostatic and Harmonic Proofs. Zenodo. [DOI Link]


## Validation Scripts (PPT 3.0 & PPT-Atoms)

The following Python scripts provide reproducible mathematical validations of key predictions in Plasma Pressure Theory (PPT) 3.0 and related atomic-scale modeling. They demonstrate the unified scaling across subatomic, molecular, nuclear, and macroscopic phenomena.

| Script Filename                          | Topic / Phenomenon                          | Brief Description                                      |
|------------------------------------------|---------------------------------------------|--------------------------------------------------------|
| proton_radius.py                         | Proton Radius Puzzle                        | Hydrostatic compression & Absolute Zero-State Volume   |
| he4_binding.py                           | Helium-4 Binding Energy                     | Tetrahedral packing & nuclear stability                |
| c12_cluster.py                           | Carbon-12 Stability                         | Fractal alpha-clustering & hexagonal harmonic lock     |
| u235_fission.py                          | Fission Yield                               | Fluid cavitation / decompression mechanics             |
| h2o_geometry.py                          | Water Bond Angle                            | Pressure equilibrium & 3D node crushing                |
| ionization_baselines.py                  | H, He, Li Ionization                        | Sub-atomic node displacements                          |
| symmetry_breaks_p2.py                    | Period 2 Ionization (Li–Ne)                 | Structural locks / symmetry breaks                     |
| shell_damping_p3.py                      | Period 3 Ionization (Na–Ar)                 | Expanded shell damping                                 |
| spectral_harmonics.py                    | Lyman & Balmer Series                       | Delta-pressure harmonic resonances                     |
| harmonic_radii.py                        | Atomic Shell Radii                          | Harmonic linear scaling                                |
| shell_saturation.py                      | $$ Capacity Rule                            | Surface area geometric limits & saturation             |
| decompression_rate.py                    | Radioactive Half-Life                       | Mechanical decompression rate (Exponential Fatigue)    |
| geometric_cleavage.py                    | Radioactive Decay Patterns                  | Anisotropic geometric cleavage                         |
| sheath_merging.py                        | Covalent & Ionic Bonding                    | Sheath fusion mechanics                                |
| noble_integrity.py                       | Octet Rule Stability                        | Perfectly symmetric saturation                         |
| zpinch_matter.py                         | Matter Inception (Solid Phase)              | Z-pinch-like condensation from plasma pressure         |

**Notes:**
- Core PPT 3.0 validations included in this release: `proton_radius.py`, `decompression_rate.py` (half-lives), and the macro gravity script (not listed here as it's already bundled separately).
- Many of these (~20 total) will receive full expansion and documentation in the upcoming **PPT-Atoms** paper/repo.
- All scripts use the fixed universal constants from PPT 3.0 (ρ_univ = 2.3 × 10¹⁷ kg/m³, R₀ = 1.25 fm, Φ_ppt = 2.223, etc.).
- Run with Python 3 + numpy/matplotlib (no exotic dependencies).

Feel free to explore the code for derivations matching Table 1 in the paper and beyond!
