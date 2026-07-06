import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model

plt.style.use('dark_background')

df = pd.read_csv('references/LinearRegression/data.csv')

styles = {
    'fontweight' : 'bold',
    'fontsize' : 18
}

x = df.area
y = df.price

plt.xlabel('Area')
plt.ylabel('Price')
plt.title('House Scatter plot')

plt.scatter(x, y, marker='*', s=100)

reg = linear_model.LinearRegression()
reg.fit(df[['area']], y)

print(reg.predict(np.array([[3300]])))
plt.tight_layout()
plt.show()