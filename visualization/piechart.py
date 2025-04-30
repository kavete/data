# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:05:50 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

number = np.array([35, 25, 25, 15])
fruits = ["Appples", "Bananas", "Cherries", "Dates"]
myexplode = [0.2, 0, 0, 0]
colors= ["green", "yellow", "red", "blue"]

plt.pie(number, labels = fruits, startangle= 30, explode=myexplode, colors=colors)
plt.legend(title="Fruits")
plt.show()