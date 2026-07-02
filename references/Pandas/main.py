import pandas as pd

df = pd.read_csv("references/Pandas/sample-data.csv")
print(df)

# Selection by column

print(df['Name'].to_string())