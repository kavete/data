import numpy as np

arr = np.array([1,2,3])

print(arr.dtype)

# String array

s_arr = np.array([1, 2, 3], dtype='S')
print(s_arr)
print(s_arr[0])

#Size for i, u, f, S, U
# 4 bytes integer
sized_arr = np.array([5, 6, 7, 8], dtype='i4')

print(sized_arr)

#Copies
float_arr = np.array([1.1, 2.6, 7.4, 6.4])
print(float_arr)

new_arr = float_arr.astype('i')
# or 
new_arr = float_arr.astype(int)
print(new_arr)