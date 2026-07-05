import matplotlib.pyplot as plt
import numpy as np

categories = np.array(['Grains', 'Fruit', 'Vegetable', 'Protein', 'Dairy', 'Sweets'])
values = [4, 3, 2, 5, 3, 1]

plt.title('Bar Chart', fontweight='bold')
plt.xlabel('Categories', fontweight='bold')
plt.ylabel('Values', fontweight='bold')

plt.bar(categories, values, color='green')
plt.show()