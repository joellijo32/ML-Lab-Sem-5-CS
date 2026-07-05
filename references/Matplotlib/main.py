import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([23, 56, 3, 5])
y2 = np.array([34, 7, 25, 8])
y3 = np.array([2, 4, 6, 25])

plt.title("Simple graph", 
        fontsize='20',
        family='Arial',
        fontweight='bold',
        color='blue')
plt.xlabel('Year', fontsize=20,
           family='Arial',
           color='green',
           fontweight='bold')
plt.ylabel('Students', fontsize=20,
           family='Arial',
           color='green',
           fontweight='bold')
plt.xticks(x)
plt.tick_params(axis='both', colors='magenta')


plt.plot(x, y1, marker='*', markersize='8')
plt.plot(x, y2, marker='*', markersize='8')
plt.plot(x, y3, marker='*', markersize='8')

plt.show()