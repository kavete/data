# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:38:45 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array([5, 7, 8, 1, 2, 17,9, 2])
y = np.array([99, 86, 87, 108, 111, 86, 87, 103])
colors = np.array(["red", "green", "yellow", "blue", "hotpink", "purple", "cyan", "orange"])

plt.scatter(x,y, c=colors)

x2= np.array([2, 2, 8, 1, 15, 8, 12, 9])
y2= np.array([100, 105, 84, 104, 90, 99, 90, 95])

colors2 = np.array([0, 10, 20, 30, 40, 50, 60, 70])
sizes = np.array([20, 50, 15, 45, 60, 100, 30, 80])
#plt.scatter(x2, y2, color='green')
plt.scatter(x2, y2,c= colors2, cmap="twilight", s =sizes, alpha=0.5)
plt.show()