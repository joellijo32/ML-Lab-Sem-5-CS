import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model


plt.style.use('dark_background')

df = pd.read_csv('references/LinearRegression/data.csv')

x = df.area
y = df.price

plt.scatter(x, y, marker='*', s=100)
plt.show()