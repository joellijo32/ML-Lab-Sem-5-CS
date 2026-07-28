import numpy as np
from sklearn.datasets import fetch_california_housing
import pandas as pd

data = fetch_california_housing()
df = pd.DataFrame(data, columns=data.feature_names)
print(df)