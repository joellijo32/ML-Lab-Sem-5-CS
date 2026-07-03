import numpy as np

# Broadcasting (different dimensions array operations)
# Either the two corresponding must be the same, or one of them must be one

array1 = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
])

array2 = np.array([
    [1], 
    [2], 
    [3], 
    [4]
])

print(array1.shape)
print(array2.shape)
print("Multiplication:\n", array1*array2)

# Multiplication table:

array1 = np.array([
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
])

array2 = np.array([
    [1],
    [2],
    [3],
    [4],
    [5],
    [6],
    [7],
    [8],
    [9],
    [10]
])

print("\nMultiplication Table:\n", array1*array2)