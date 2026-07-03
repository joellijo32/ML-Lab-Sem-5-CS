import numpy as np

# Scalar arithmetic

array = np.array([1, 2, 3])

print("Array + 3:", array+3)

print("Array / 2:", array/2)

print("Array ^ 5:", array**5)

# Vectorized math functions

array = np.array([1.2, 4.6, 6.1])

print("Square root:", np.sqrt(array))

print("Rounding:", np.round(array))

print("Round down:", np.floor(array))

print("Round up:", np.ceil(array))

print("Pi:", np.pi)

radii = np.array([1, 2, 3])

print("Area:", (np.pi * (radii**2)))

# Element-wise arithmetic

array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])

print("Sum:", array2 + array1)

print("Multiplication:", array1*array2)

print("Division:", array1/array2)

# Comparison operators

scores = np.array([91, 33, 63, 100, 13, 71])

print("Full marks:", scores==100)

scores[scores<60] = 0

print("Fail:", scores)