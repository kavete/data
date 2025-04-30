import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

#Slice from index 1 to index 5
#Index 5 not included
print(arr[1:5])

#Index 4 to end
print(arr[4:])

#start to index 4
print(arr[:4])

#Negative slicing
# Two  elements, Last not included
print(arr[-3:-1])

#Three last elemnts
print(arr[-3:])

#step
#Index 1 to 5 (excluded) with step of 2
print(arr[1:5:2])

#start to end with step of 2
print(arr[::2])

#slice 2-D arrays
two_d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

#Return Index 1 to 3 in the second element
print(two_d[1, 1:4])

#From both elements, return index 2
print(two_d[0:2, 2] )