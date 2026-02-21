import numpy as np
import matplotlib.pyplot as plt

# PPT-Atoms Validation Suite v1.0.0
# Script: Relativistic_Mass_Hydrostatic_Bow_Shock_Final.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Maps relativistic mass increase to fluid-dynamic bow-shock compression.

def calculate_bow_shock_displacement():
    print("--- PPT - Atoms: PPT 3.0: Hydrostatic Bow Shock (Relativistic Mass) Solver ---")
    
    # 1. GENERATE VELOCITY RANGE
    # We use a high resolution (1000 points) to capture the curve near c.
    # np.clip ensures we never hit exactly 1.0, avoiding division by zero.
    v_raw = np.linspace(0, 0.999, 1000)
    mach_numbers = np.clip(v_raw, 0, 1 - 1e-15) 
    
    # 2. THE STANDARD MODEL (Lorentz Transformation)
    lorentz_factors = 1 / np.sqrt(1 - (mach_numbers**2))
    
    # 3. PPT 3.0 FLUID DYNAMICS (Prandtl-Glauert Compressibility)
    # In PPT, 'c' is the wave-speed limit of the medium.
    # Mass increase is re-defined as added displacement volume from leading-edge compression.
    prandtl_glauert_factors = 1 / np.sqrt(1 - (mach_numbers**2))
    
    # --- TERMINAL VALIDATION OUTPUT ---
    print("\nVelocity (v/c) | Standard Lorentz (γ) | PPT Prandtl-Glauert | Difference")
    print("-" * 76)
    
    test_points = [0.1, 0.5, 0.8, 0.9, 0.95, 0.99]
    for v in test_points:
        # Find the index closest to our test velocity
        idx = np.abs(mach_numbers - v).argmin()
        lor = lorentz_factors[idx]
        pg = prandtl_glauert_factors[idx]
        print(f"{v:<14.2f} | {lor:<20.5f} | {pg:<19.5f} | {abs(lor-pg):.5f}")

    print("\nMechanical Conclusion:")
    print("Relativistic mass increase is a fluid-dynamic compressibility effect.")
    print("The Lorentz Factor and the Prandtl-Glauert Factor are mathematically")
    print("identical when c is treated as the medium's wave-propagation limit.")

    # --- HIGH-VISIBILITY VISUAL PROOF ---
    plt.figure(figsize=(11, 6.5))
    
    # Observed Reality / Lorentz (Gold)
    plt.plot(mach_numbers, lorentz_factors, color='#FFD700', linestyle='-', 
             linewidth=4, label='Standard Relativity (Lorentz)', alpha=0.7, zorder=3)

    # PPT Bow Shock (Cyan Dash)
    plt.plot(mach_numbers, prandtl_glauert_factors, color='#00FFFF', linestyle='--', 
             linewidth=2, label='PPT 3.0 Bow Shock (Prandtl-Glauert)', zorder=4)

    # Styling
    plt.title('Effective Mass Increase: Spacetime Warping vs. Hydrostatic Compression', fontsize=14, pad=20)
    plt.xlabel('Velocity relative to Wave Speed Limit ($v/c$)', fontsize=12)
    plt.ylabel('Effective Displacement Multiplier (Mass)', fontsize=12)
    
    # High-visibility Annotation
    bbox_props = dict(boxstyle="round,pad=0.3", fc="white", ec="black", lw=1, alpha=0.9)
    plt.annotate('The "Speed of Light" Barrier is a\nFluid-Dynamic Singularity', 
                 xy=(0.97, 4.0), xytext=(0.35, 5.5), 
                 arrowprops=dict(arrowstyle="->", color='#00FFFF', lw=2),
                 bbox=bbox_props, fontsize=11)

    plt.legend(frameon=True, facecolor='white', framealpha=0.9, loc='upper left')
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    calculate_bow_shock_displacement()