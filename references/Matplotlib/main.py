import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

x1 = np.array([0, 1, 1, 2, 3, 4, 5, 6, 7, 7, 8])
y1 = np.array([55, 60, 65, 62, 68, 70, 75, 78, 82, 85, 87])

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 8])
y2 = np.array([50, 58, 65, 70, 72, 78, 83, 88, 92, 95, 97])

styles = {
    'fontweight': 'bold',
    'fontsize' : 18,
    }

plt.xlabel('Hours Studied', **styles)
plt.ylabel('Test Scores', **styles)
plt.title('Scatter Plot', **styles)


plt.scatter(x1, y1,
            marker='o',
            s=150,
            color='cyan',
            alpha=0.5,
            label='Class A'
)
plt.scatter(x2, y2,
            marker='o',
            s=150,
            color='#9fe0d8',
            alpha=0.5,
            label='Class B'
)
plt.legend();
plt.show()