# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:51:00 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(100, size=(100))
y = np.random.randint(100, size=(100))

colors= np.random.randint(100, size=(100))
sizes = 10 * np.random.randint(100, size=(100))

#Scatter plot with colormap, different sizes fro each plot and faded 50%
plt.scatter(x, y, c =colors, s =sizes, alpha=0.5, cmap='nipy_spectral')

#Show the colorbar
plt.colorbar()
plt.show()
