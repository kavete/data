import numpy as np

arr = np.array([1, 2, 3, 4])

#Return index 0 element
print(arr[0])

#Add first and second element
print(arr[0] + arr[1])

#2 D and 3 D indexing
two_d = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("Second element in first row:", two_d[0,1])

three_d = np.array([[[1,2,3,4], [5, 6, 7, 8]], [[9, 10, 11, 12], [13, 14, 15, 16]]])
print(three_d[0,1,2])

# Negative Indexing
print("Last element from second dimendion:", two_d[1,-1])