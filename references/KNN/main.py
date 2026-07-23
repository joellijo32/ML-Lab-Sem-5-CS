import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Datafram split into three, with respective classes

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[100:]

# Plotting all three classes

x0 = df0['sepal length (cm)']
y0 = df0['sepal width (cm)']

x1 = df1['sepal length (cm)']
y1 = df1['sepal width (cm)']

x2 = df2['sepal width (cm)']
y2 = df2['sepal width (cm)']

plt.xlabel('sepal length (cm)')
plt.ylabel('sepal width (cm)')
plt.scatter(x0, y0, label='df0', alpha=0.7, s=100)
plt.scatter(x1, y1, label='df1', alpha=0.7, s=100)
plt.scatter(x2, y2, label='df2', alpha=0.7, s=100)
plt.legend()
plt.tight_layout()
plt.show()

