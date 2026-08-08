import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing

california = fetch_california_housing()
df = pd.DataFrame(california.data, columns=california.feature_names)
df['MedHouseVal'] = pd.Series(california.target)

print(df.head())


