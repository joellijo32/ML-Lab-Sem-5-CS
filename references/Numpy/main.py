import numpy as np

array = np.array([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12], 
    [13, 14, 15, 16]
])

# array[start: end: step]

print("First row:", array[0:1])

print("\nStep 2:\n", array[::2])

print("\nReverse\n", array[::-1])

print("\nReverse Step 2\n", array[::-2])

print("\nFirst Column\n", array[:,0])

print("\nStep 2 Column\n", array[:, ::2])

print("\nReverse Column\n", array[:, ::-1])

print("\nFirst two rows and columns\n", array[:2, :2])