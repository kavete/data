# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 17:55:16 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.array(['A', 'B', 'C', 'D'])
y = np.array([3, 8, 1, 10])


plt.subplot(1, 2, 1)
plt.barh(x, y, color="cyan", height=0.5)

plt.subplot(1, 2, 2)
plt.bar(x, y, width=0.3)
plt.show()