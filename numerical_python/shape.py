import numpy as np

arr = np.array([[[1,2,3,4], [5,6,7,8]], [[9,10,11,12], [13,14,15,16]]])

print(arr.shape)

#1-D to 2-D

arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
newarr = arr.reshape(4,3)
print(newarr)
print(">>>")
#1-D to 3-D
newarr = arr.reshape(2,3,2)
print(newarr, "\n")

# Unknown dimension
newarr = arr.reshape(3,2,-1)
print(newarr)

#Flattening
#Converting a multidemensional array into a 1-D array

flat_array = newarr.reshape(-1)
print(flat_array)