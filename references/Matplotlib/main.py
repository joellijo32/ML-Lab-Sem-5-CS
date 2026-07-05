import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

scores = np.random.normal(loc=80, scale=10, size=100)
scores = np.clip(scores, 0, 100)

styles = {
    'fontweight' : 'bold',
    'fontsize' : 18
}

plt.figure(figsize=(10, 6))
plt.xlabel('Scores', **styles)
plt.ylabel('No. of students', **styles)
plt.title('Histogram', **styles)

plt.hist(scores, bins=10,
         color='lightgreen',
         edgecolor='black');
plt.show()
