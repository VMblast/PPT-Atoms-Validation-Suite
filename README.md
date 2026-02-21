# PPT-Atoms-Validation-Suite
Computational Verification of the Plasma Pressure Theory (PPT) Model


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
