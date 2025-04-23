# -*- coding: utf-8 -*-
"""
Created on Fri Apr 18 12:36:00 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.array([60, 70, 80, 95, 100])
y = np.array([240, 260, 270, 275, 300])

font1= {'family': 'serif', 'color': 'blue', 'size': 20}
font2 = {'family': 'serif', 'color': 'darkred', 'size': 10}

plt.plot(x, y)
plt.title("Sport's Watch data", fontdict=font1, loc='right')
plt.xlabel("Average Pulse", fontdict=font2)
plt.ylabel("Calorie Burnage", fontdict = font2)

plt.show()