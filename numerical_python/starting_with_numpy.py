# -*- coding: utf-8 -*-
"""
Created on Fri Apr 25 15:33:15 2025

@author: brian
"""

import numpy as np

arr = np.array([1, 2, 3, 4])
arr2 = np.array((5, 6, 7, 8))
#arr3 = np.array({5, 8, 8, 9, 6})
arr4 = np.array(["Bob", "Job", "Doe", "Ian", "Joe"])
print(arr)
print(arr2)
print(arr4)
print(arr4[0])

# 2-D
two_d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(two_d)

# 3-D

three_d = np.array([[[1,2,3,4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(three_d)

print(three_d.ndim)
print(two_d.ndim)

# Higher Dimension
high_d = np.array([1, 2, 3, 4], ndmin=5)
print(high_d)