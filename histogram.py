# -*- coding: utf-8 -*-
"""
Created on Wed Apr 23 18:02:44 2025

@author: brian
"""

import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)

plt.show()