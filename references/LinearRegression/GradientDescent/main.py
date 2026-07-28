import numpy as np
from sklearn.datasets import fetch_california_housing
import pandas as pd
from sklearn.linear_model import LinearRegression

data = fetch_california_housing()
df = pd.DataFrame(data.data, columns=data.feature_names)
df['MedHouseVal'] = data.target

X = df['AveRooms'][:5000]
y = df['MedHouseVal'][:5000]

model = LinearRegression()

