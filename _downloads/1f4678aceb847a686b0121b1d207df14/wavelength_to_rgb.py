"""
Wavelength to RGB
=================
An approximate conversion from wavelength to RGB values for plotting.
"""

import numpy as np

import mirage.vis as mrv

wavelengths = np.linspace(400, 700, 1000) * 1e-9
rgbs = mrv.wavelength_to_rgb(wavelengths).reshape(1, -1, 3)

import matplotlib.pyplot as plt

plt.figure(figsize=(6, 2))
plt.imshow(rgbs, extent=[wavelengths.min(), wavelengths.max(), 0, 50])
plt.yticks([])
plt.xlabel("Wavelength (nm)")
plt.title("Wavelength to RGB")
plt.gca().invert_xaxis()
plt.show()
