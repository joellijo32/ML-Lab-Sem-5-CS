import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.style.use('dark_background')
plt.figure(figsize=(10, 6))

styles = {
    'fontweight' : 'bold',
    'fontsize' : 18
}

df = pd.read_csv('references/Pandas/sample-data.csv')

counts =df['Type1'].value_counts(ascending=True)

plt.barh(counts.index, counts.values, color='gold')
plt.xlabel('Count', **styles)
plt.ylabel('Types', **styles)
plt.title('No. of pokemon by type', **styles)
plt.tight_layout()
plt.show()