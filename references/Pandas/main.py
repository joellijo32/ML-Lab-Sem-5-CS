import pandas as pd

df = pd.read_csv('references/Pandas/sample-data.csv')

# Filtering

tall_pokemon = df[df['Height'] >= 2]
print("Tall Pokemon:\n", tall_pokemon)

heavy_pokemon = df[df['Weight'] > 100]
print("\nHeavy Pokemon\n",heavy_pokemon)

legendary_pokemon = df[df['Legendary'] == True]
print("\nLegendary Pokemon\n",legendary_pokemon);

water_pokemon = df[(df['Type1'] == 'Water') | (df['Type2'] == 'Water')] 
print("\nWater Pokemon:\n", water_pokemon)

fire_fly_pokemon = df[(df['Type1'] == 'Fire') & (df['Type2'] == 'Flying')]
print("\nFire and Fly Pokemon:\n", fire_fly_pokemon)