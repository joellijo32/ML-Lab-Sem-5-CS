import pandas as pd

df = pd.read_csv("references/Pandas/sample-data.csv", index_col='Name')


# Selection by column

# print(df.loc["Bulbasaur":'Blastoise', [ "Height", "Weight"]])
name = input("Enter pokemon name: ")

try:
    print(df.loc[name])
except KeyError:
    print(f"{name} not found")