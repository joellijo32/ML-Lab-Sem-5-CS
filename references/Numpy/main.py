import numpy as np

# Random numbers

rng =  np.random.default_rng(seed=2) # Seed fixes the results once generated. (Minecraft analogy)
np.random.seed(21)

#rng.integers(start idx, end idx (exclusive), dimensions (no. of numbers))
print("Integer:\n", rng.integers(low=1, high=101, size=(3,3)))

print("\nFloating:\n", np.random.uniform(low=-1, high=1, size=(5,2)))


# Array shuffling

array = np.array([1, 2, 3, 4, 5])

print("\nArray:\n", array)

rng = np.random.default_rng()

rng.shuffle(array)

print("\nShuffled Array:\n", array)

fruits = np.array(['apple', 'orange', 'banana', 'pineapple', 'tomato'])

print("\nFruits:\n", fruits)

fruit = rng.choice(fruits, size=(4,4))
print("\nChoice:\n", fruit)
