import numpy as np

# PPT-Atoms Validation Suite v1.0.0
# Script: Lithium_Ionization_Geometric_Solver.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Calculates Lithium's first ionization energy using fluid-dynamic volumetric shielding.

def solve_lithium_ionization():
    print("--- PPT - Atoms: PPT 3.0: Lithium Ionization Geometric Solver ---")
    
    # 1. BASELINE HARMONIC TENSION
    # The maximum structural tension at the n=1 boundary (Hydrogen baseline)
    e_base_tension = 13.605  # eV
    
    # 2. HYDROSTATIC BOUNDARY EXPANSION
    # The outer node is in the n=2 shell. Pressure drops geometrically by 1/n^2.
    n_outer = 2
    boundary_expansion_drop = 1 / (n_outer**2)  # 0.25
    
    # Baseline n=2 tension (without core adjustments)
    e_n2_baseline = e_base_tension * boundary_expansion_drop
    print(f"1. Unshielded n={n_outer} Boundary Tension: {e_n2_baseline:.4f} eV")
    
    # 3. VOLUMETRIC SHIELDING (Replacing Z_eff)
    # Core has 3 displacement units. Inner shell has 2 pinned nodes.
    # In PPT 3.0, displacement is volume. Volumetric shielding scales geometrically.
    # The permeability of the inner Double Layer is proportional to the cube root of the node count.
    inner_nodes = 2
    volumetric_permeability = np.cbrt(inner_nodes)  # ~1.2599
    
    # The structural pinning force scales by the square of the permeability 
    # (analogous to how standard physics squares Z_eff, but derived from geometric area/volume ratios)
    geometric_pinning_multiplier = volumetric_permeability**2  # ~1.5874
    
    print(f"2. Inner Double Layer Nodes: {inner_nodes}")
    print(f"3. Volumetric Permeability Factor: {volumetric_permeability:.4f}")
    
    # 4. DETERMINISTIC CALCULATION
    e_li_pred = e_n2_baseline * geometric_pinning_multiplier
    
    # 5. VALIDATION
    real_li_nist = 5.3917 # eV
    accuracy = (1 - abs(e_li_pred - real_li_nist) / real_li_nist) * 100
    
    print("\n--- Validation Results ---")
    print(f"Experimental (NIST): {real_li_nist:.4f} eV")
    print(f"PPT 3.0 Deterministic: {e_li_pred:.4f} eV")
    print(f"Predictive Accuracy:   {accuracy:.2f}%")
    
    print("\nMechanical Conclusion:")
    print("Lithium's ionization energy is determined by the 1/n² hydrostatic pressure drop, ")
    print("multiplied by the volumetric permeability of its 2-node inner double layer.")

if __name__ == "__main__":
    solve_lithium_ionization()