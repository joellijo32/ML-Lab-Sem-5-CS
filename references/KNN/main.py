import pandas as pd
from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['target'] = iris.target

# Datafram split into three, with respective classes

df0 = df[df.target == 0]
df1 = df[df.target == 1]
df2 = df[100:]

# Plotting all three classes
'''
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
'''

# Train test split

x = df.drop(['target'], axis='columns')
y = df.target
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

# Model training and prediction

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)

score = knn.score(X_test, y_test)
print("Prediction score:", score)

y_pred = knn.predict(X_test)
cm = confusion_matrix(y_test, y_pred)
print(cm)
