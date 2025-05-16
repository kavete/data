# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 12:16:32 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

#x = np.array([0, 1, 2, 3])
y = np.array([5,7,2,3])

#plt.plot(y, marker='o')
#plt.plot(y, marker='*')
#plt.plot(y, ls= 'dotted', lw="5")
plt.plot(y, linestyle= 'dotted', linewidth="10")

#Marker line style and color
#plt.plot(y, 'o--y', ms=20, mfc='#4caf50')
plt.show()