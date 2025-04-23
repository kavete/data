# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 12:45:45 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

x= np.array([0,1,1,2,3,5,8,11])
y = np.array([0,1,1,2,3,5,8,11])
plt.subplot(1,2,1)
plt.plot(y)
plt.title("Fibonnacci")
#plt.grid(axis='both')
#plt.grid(axis='y') # or x

plt.subplot(1, 2, 2)
plt.plot(x, y)
plt.title("grid")
plt.grid(color='red', linestyle='--', linewidth=2)

plt.suptitle("Vis a Vis")
plt.show()