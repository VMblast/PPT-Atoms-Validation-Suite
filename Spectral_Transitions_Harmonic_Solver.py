import numpy as np

# PPT-Atoms Validation Suite v1.0.0
# Script: Spectral_Transitions_Harmonic_Solver.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Calculates hydrogen spectral lines as harmonic pressure node transitions.

def calculate_harmonic_transition():
    print("--- PPT - Atoms: PPT 3.0: Harmonic Node Transition Solver (Hydrogen) ---")
    
    # Ground state pinning pressure equivalent (eV)
    # This represents the maximum structural tension at the n=1 boundary
    E_ground_H = 13.605 
    
    # 1. LYMAN-ALPHA (n=2 to n=1)
    # In PPT 3.0, moving from the 2nd harmonic node to the ground state 
    # releases 75% of the pinning tension (1/1^2 - 1/2^2 = 0.75).
    n_low_lyman = 1
    n_high_lyman = 2
    
    delta_factor_lyman = (1 / n_low_lyman**2) - (1 / n_high_lyman**2)
    E_lyman_alpha = delta_factor_lyman * E_ground_H
    
    print(f"\n1. Lyman-Alpha Transition (n={n_high_lyman} -> n={n_low_lyman}):")
    print(f"   PPT Predicted Energy: {E_lyman_alpha:.3f} eV")
    print("   Experimental Value:   10.20 eV")
    
    # 2. GENERAL TRANSITION FUNCTION
    def transition_energy(n_low, n_high, E_base):
        # Calculates the tension difference between two specific harmonic pressure boundaries
        if n_high > n_low:
            return E_base * ((1 / n_low**2) - (1 / n_high**2))
        return 0

    print("\n2. General Series Validation (Tension Release Matrix):")
    
    # Lyman Beta (n=3 -> n=1)
    e_lyman_beta = transition_energy(1, 3, E_ground_H)
    print(f"   n=3 -> n=1 (Lyman-Beta):   {e_lyman_beta:.2f} eV  (Exp: 12.09 eV)")
    
    # Balmer Alpha (n=3 -> n=2)
    e_balmer_alpha = transition_energy(2, 3, E_ground_H)
    print(f"   n=3 -> n=2 (Balmer-Alpha):  {e_balmer_alpha:.2f} eV  (Exp:  1.89 eV)")

if __name__ == "__main__":
    calculate_harmonic_transition()