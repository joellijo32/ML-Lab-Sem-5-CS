import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 15, 20, 25, 30])

plt.title("Grid Plot")
plt.xlabel("X axis")
plt.ylabel('Y axis')
plt.grid(axis='y', color='green', linestyle='-.')

plt.plot(x, y, marker='*', markersize='9')
plt.show()