import matplotlib.pyplot as plt
import numpy as np

plt.style.use('dark_background')

categories = np.array(['Freshman', 'Sophomores', 'Juniors', 'Seniors'])
values = np.array([300, 250, 275, 225])

colors= np.array(['red', 'yellow', 'blue' ,'green'])
plt.title('Pie Chart', fontweight='bold')


plt.pie(values, labels=categories,
        autopct='%1.1f%%',
        colors=colors,
        explode=[0, 0, 0, 0.2],
        shadow=True,
)
plt.show()