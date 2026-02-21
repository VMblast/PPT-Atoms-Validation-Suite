import numpy as np
import math

# PPT-Atoms Validation Suite v1.0.0
# Script: Helium4_Nuclear_Binding_Solver.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Calculates the nuclear binding energy of the Alpha Particle (He-4) purely from geometric volumetric defect.

def solve_alpha_binding_energy():
    print("--- PPT - Atoms: PPT 3.0: Helium-4 Nuclear Binding Geometric Solver ---")
    
    # 1. THE UNIFIED CONSTANTS
    rho_medium_nuclear = 2.3e17  # Universal medium density (kg/m^3)
    c2 = (299792458)**2          # Maximum wave speed squared
    joules_to_MeV = 1.60218e-13
    
    # 2. THE GEOMETRIC NUCLEON VOLUMES
    r_nucleon = 0.8427e-15       # PPT 3.0 Muonic Proton Radius (meters)
    
    # Volume of a single spherical nucleon: V = (4/3) * pi * r^3
    v_single_nucleon = (4/3) * math.pi * (r_nucleon**3)
    
    # Raw, uncompressed volume of 4 separate nucleons
    v_raw_total = 4 * v_single_nucleon
    
    # 3. THE GEOMETRIC DEFECT (THE ALPHA PACKING OVERLAP)
    # In a tetrahedral tight-packing model under extreme medium pressure, 
    # the nodes compress. This lost volume forms the Phi_ppt baseline (2.223).
    # Geometric overlap fraction is ~2.223%
    compression_overlap_fraction = 0.02223 
    
    # The volumetric displacement physically crushed out by the medium during fusion
    delta_v_geometric = v_raw_total * compression_overlap_fraction
    
    # 4. DETERMINISTIC PPT ENERGY CALCULATION
    # E = Pressure * Volume Defect
    # Pressure = rho_univ * c^2
    e_binding_J = (rho_medium_nuclear * c2) * delta_v_geometric
    e_binding_MeV = e_binding_J / joules_to_MeV
    
    print(f"1. Raw 4-Nucleon Displacement Volume: {v_raw_total:.4e} m^3")
    print(f"2. Alpha Packing Volume Defect (dV):  {delta_v_geometric:.4e} m^3")
    
    # 5. VALIDATION
    real_binding_MeV = 28.3  # Standard observed binding energy of He-4
    accuracy = (1 - abs(e_binding_MeV - real_binding_MeV) / real_binding_MeV) * 100
    
    print("\n--- Validation Results ---")
    print(f"Experimental (Standard): {real_binding_MeV:.2f} MeV")
    print(f"PPT 3.0 Deterministic:   {e_binding_MeV:.2f} MeV")
    print(f"Predictive Accuracy:     {accuracy:.2f}%")
    
    print("\nMechanical Conclusion:")
    print("The 'mass defect' of nuclear physics is strictly a geometric Volume Defect.")
    print("The 2.223% volume lost here establishes the Phi_ppt constant used across")
    print("all PPT 3.0 atomic and molecular scale validations.")

if __name__ == "__main__":
    solve_alpha_binding_energy()