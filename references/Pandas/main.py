import pandas as pd

data = {
    'Name' : ['Joel', 'Joshua', 'Jiss'],
    'Age' : [19, 45, 23]
}

df = pd.DataFrame(data, index=['guy 1', 'guy 2', 'guy 3'])
print(df.loc['guy 1'])
