import pandas as pd

data = [234, 45,134, 5,54,76]

series = pd.Series(data, index=['a', 'b', 'c', 'd', 'e', 'f'])

print(series[series >= 100])