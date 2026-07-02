import pandas as pd

df = pd.read_csv('references/Pandas/sample-data.csv')

# Aggregrate function

# Whole DataFrame

print("\nMean: \n",df.mean(numeric_only=True))

print("\nSum: \n", df.sum(numeric_only=True))

print("\nMininum: \n", df.min(numeric_only=True))

print("\nMaximum: \n", df.max(numeric_only=True))

print("\nCount: \n", df.count())

# Single column

print("\nHeight: \n", df['Height'].mean())

print("\nSum: \n", df['Weight'].sum())

print("\nMininum: \n", df['Weight'].min())

print("\nMaximum: \n", df['Height'].max())

print("\nCount: \n", df['Type2'].count())

group = df.groupby('Type1')

print("\nGroup by: \n", group['Height'].mean())

print("\nSum \n", group["Height"].sum())

print("\nMinimum \n", group['Weight'].min())

print("\nCount \n", group["Weight"].count())