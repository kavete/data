import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x_copy = arr.copy()
y_view = arr.view()

print(arr)
print(x_copy)
print(y_view)

#Changing the copy doesn't affect the original
#Neither does changing the original affect the copy
x_copy[0] = 31

print(arr)
print(x_copy)

# Changing either the view or the original affects the other
y_view[1] = 53

print(y_view)
print(arr)

#Check if the array owns the data
# Returns none if it owns the data - No base
print(x_copy.base)
print(y_view.base)