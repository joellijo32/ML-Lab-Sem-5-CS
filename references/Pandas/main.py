import pandas as pd

df = pd.read_csv('references/Pandas/sample-data.csv')

# Drop a column
df = df.drop(columns=['Legendary', 'No'])
print("\nDrop a column: \n", df)

# Missing Data
missing_df = df.dropna(subset=['Type2']) # Drop if missing
print("\nMissing Data: \n", missing_df.to_string())

# Filling missing
filling_df = df.fillna({
    'Type2' : 'None'
})
print("\nFilling Data: \n", filling_df.to_string())

# Inconsistent Value fix
df['Type1'] = df['Type1'].replace({
    'Grass' : 'GRASS'
})
print("\nInconsistent fix: \n", df[df['Type1'] == 'GRASS'].to_string())

df['Name'] = df['Name'].str.lower()
print("\nAll names capital: \n", df)

# Fix data types

new_df = pd.read_csv('references/Pandas/sample-data.csv')
new_df['Legendary'] = new_df['Legendary'].astype(bool)
print("\nData Type Change: \n", new_df)

# duplicate data

new_df = pd.read_csv('references/Pandas/sample-data.csv')
new_df = df.drop_duplicates()
print("\nNo duplicates: \n", new_df)
