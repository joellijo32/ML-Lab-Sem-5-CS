import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([23, 56, 3, 5])
y2 = np.array([34, 7, 25, 8])
y3 = np.array([2,4,6,25])

line_style = dict(
marker='o',
markerfacecolor='crimson',
markeredgecolor='black',
markersize=10,
linestyle='solid',
linewidth=3,
)

plt.plot(x, y1, color='blue',  **line_style)

plt.plot(x, y2, color='green', **line_style)

plt.plot(x, y3, color='red', **line_style)

plt.title("Simple graph")
plt.show()