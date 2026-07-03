import numpy as np

# Aggregate Function

array = np.array([
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
])

print("Sum:", np.sum(array))

print("Mean:", np.mean(array))

print("Standard Deviation:", np.std(array))

print("Variance:", np.var(array))

print("Mininum:", np.min(array))

print("Maximum:", np.max(array))

print("Position of min:", np.argmin(array))

print("Position of max:", np.argmax(array))

print("Sum of columns:", np.sum(array, axis=0))

print("Sum of rows:", np.sum(array, axis=1))