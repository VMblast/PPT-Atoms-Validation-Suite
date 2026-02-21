import numpy as np
import matplotlib.pyplot as plt

# PPT-Atoms Validation Suite v1.0.0
# Script: Fasifiable_Cleavage_And_Alpha_Decay.py
# Author: Vladimir Milosevic
# Theory: Plasma Pressure Theory (PPT) 3.0
# Description: Alpha Decay Geometric Cleavage Simulation


# =============================================================================
# PPT-ATOMS: ALPHA DECAY GEOMETRIC CLEAVAGE SIMULATION
# =============================================================================

# Set aesthetic style
plt.style.use('dark_background')
fig = plt.figure(figsize=(14, 7))
fig.suptitle('Falsifiable Prediction: Alpha Decay Emission Topology', 
             fontsize=18, fontweight='bold', color='white', y=0.95)

n_events = 5000  # Number of simulated alpha particle emissions

# -----------------------------------------------------------------------------
# MODEL A: STANDARD PHYSICS (Isotropic Quantum Probability)
# -----------------------------------------------------------------------------
# Alpha particles "tunnel" out randomly in all 360 degrees
phi_std = np.random.uniform(0, 2 * np.pi, n_events)
costheta_std = np.random.uniform(-1, 1, n_events)
theta_std = np.arccos(costheta_std)

x_std = np.sin(theta_std) * np.cos(phi_std)
y_std = np.sin(theta_std) * np.sin(phi_std)
z_std = np.cos(theta_std)

ax1 = fig.add_subplot(121, projection='3d')
ax1.set_facecolor('#0a0a0a')
ax1.scatter(x_std, y_std, z_std, s=15, c='#457b9d', alpha=0.6, edgecolors='none')
ax1.set_title('Standard Model: Isotropic Probability\n(Random Spherical Emission)', 
              color='white', pad=20, fontsize=12)
ax1.set_axis_off()  # Hide grid for pure particle visualization

# -----------------------------------------------------------------------------
# MODEL B: PPT-ATOMS (Anisotropic Geometric Cleavage)
# -----------------------------------------------------------------------------
# Alpha particles fracture off the geometric fault lines of a tetrahedral core
vertices = np.array([
    [1, 1, 1],
    [-1, -1, 1],
    [-1, 1, -1],
    [1, -1, -1]
]) / np.sqrt(3)

x_ppt, y_ppt, z_ppt = [], [], []

for _ in range(n_events):
    # Select a random geometric fault line
    base_vector = vertices[np.random.randint(0, 4)]
    
    # Add minor thermal/vibrational noise to the fracture vector
    noise = np.random.normal(0, 0.15, 3)
    fracture_vector = base_vector + noise
    
    # Normalize back to the surface of the emission sphere
    fracture_norm = fracture_vector / np.linalg.norm(fracture_vector)
    
    x_ppt.append(fracture_norm[0])
    y_ppt.append(fracture_norm[1])
    z_ppt.append(fracture_norm[2])

ax2 = fig.add_subplot(122, projection='3d')
ax2.set_facecolor('#0a0a0a')
ax2.scatter(x_ppt, y_ppt, z_ppt, s=15, c='#e63946', alpha=0.6, edgecolors='none')
ax2.set_title('PPT-Atoms: Geometric Cleavage\n(Directional Fault-Line Emission)', 
              color='white', pad=20, fontsize=12)
ax2.set_axis_off()

# Save and show
plt.tight_layout()
plt.subplots_adjust(top=0.85)
plt.savefig('decay_topology_falsification.png', dpi=300, facecolor='#0a0a0a')
print("Simulation complete. Image saved as: decay_topology_falsification.png")
plt.show()