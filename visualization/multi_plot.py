# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 12:30:32 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

x= np.random.randint(100, size=(10))
y1 = np.random.randint(100, size=(10))
y2 = np.random.randint(100, size=(10))

#Plot on the same axis
plt.plot(x,y1, color='b')
plt.plot(x,y2, color='y')
plt.show()

