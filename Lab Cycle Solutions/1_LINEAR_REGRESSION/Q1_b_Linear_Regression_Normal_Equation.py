import matplotlib.pyplot as plt
import pandas as pd

from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

california = fetch_california_housing()

df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = california.target

X = df[['AveRooms']]
y = df['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(
	X, y, test_size=0.2
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('\nNormal Equation\n')
print('Intercept:', model.intercept_)
print('Coefficient:', model.coef_[0])
print('Mean Squared Error:', mse)
print('R Squared (R²):', r2)
