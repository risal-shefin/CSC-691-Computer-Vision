import numpy as np
import matplotlib.pyplot as plt

def thin_lens_zi(f, z0):
    return 1 / (1/f - 1/z0)

def aperture_diameter(f, f_number):
    return f / f_number

f_list = [3, 9, 50, 200]    # focal lengths in mm
colors = ["red", "green", "blue", "orange"]

fig, axes = plt.subplots(1, 2, figsize=(12, 5)) # 2 subplots side by side
# Loop: Image distance vs Object distance for different focal lengths
for f, color in zip(f_list, colors):
    z0 = np.linspace(1.1*f, 1e4, int(4*(1e4 - 1.1*f)))
    zi = thin_lens_zi(f, z0)
    axes[0].loglog(z0, zi, label=f"f={f} mm", color=color)
    axes[0].axvline(f, linestyle="--", color=color)

# Configuring the first subplot
axes[0].set_xlabel(r"$z_0$ (mm)")
axes[0].set_ylabel(r"$z_i$ (mm)")
axes[0].set_ylim(0, 3000)
axes[0].grid(True, which="major", ls="--")
axes[0].legend()
axes[0].set_title("Image Distance vs Object Distance")


f_number_list = [1.4, 1.8, 2.8, 4.0]    # f-numbers in mm
# Loop: Aperture diameter vs Focal length for different f-numbers
for f_number, color, f_number in zip(f_list, colors, f_number_list):
    f = np.linspace(0, 1e4, int(4*1e4))
    d = aperture_diameter(f, f_number)
    axes[1].plot(f, d, label=f"f#={f_number}", color=color)

# Configuring the second subplot
axes[1].set_xlabel(r"$f$ (mm)")
axes[1].set_ylabel(r"$D$ (mm)")
axes[1].set_ylim(0, 3000)
axes[1].grid(True, which="major", ls="--")
axes[1].legend()
axes[1].set_title("Aperture Diameter vs Focal Length")

plt.tight_layout()
plt.show()