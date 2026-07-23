import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Datafram split into three, with respective classes

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[100:]


