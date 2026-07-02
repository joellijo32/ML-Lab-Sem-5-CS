import pandas as pd

df = pd.read_csv("references/Pandas/sample-data.csv", index_col='Name')


# Selection by column

# print(df.loc["Bulbasaur":'Blastoise', [ "Height", "Weight"]])
print(df.iloc[0:32:2, 0:3])