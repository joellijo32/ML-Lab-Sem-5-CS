import pandas as pd

calories = {
    'Day 1' : 45355,
    'Day 2' : 23413,
    'Day 3' : 564,
    'Day 4' : 45426
}

series = pd.Series(calories)
print(series['Day 3'])