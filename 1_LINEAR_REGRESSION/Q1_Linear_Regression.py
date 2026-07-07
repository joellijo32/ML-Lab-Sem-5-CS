import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

california = fetch_california_housing()

df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = california.target

X = df[['AveRooms']]
y = df['MedHouseVal']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

fig, ax = plt.subplots(1, 2, figsize=(10, 8))
fig.suptitle('Linear Regression')

ax[0].set_xlabel('Average Rooms')
ax[0].set_ylabel('Median House Value')
ax[0].scatter(X_test,
	      y_test,
	      color='red',
	      alpha=0.3,
	      label='Actual Test Data')
ax[0].legend()

ax[1].set_xlabel('Average Rooms')
ax[1].set_ylabel('Median House Value')
ax[1].plot(X_test,
	   y_pred,
	   label='Predicted Data')
ax[1].legend()

plt.tight_layout()
plt.show()







