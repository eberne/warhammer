# import numpy as np

import pandas as pd

df = pd.read_csv('model_data.csv')
df.rename(index={0: 'plaque_marine',
                 1: 'plaque_marine_champion',
                 2: 'plaque_marine_gunner',
                 3: 'intercessor',
                 4: 'intercessor_sergeant',
                 5: 'guardsman',
                 6: 'guardsman_sergent'},
          inplace=True)

df["Quantity"] = df['Quantity'].fillna(-1)   # in order to get astype to work
df['Quantity'] = df['Quantity'].astype(int)  # Not sure why this is necessary

fighter = 'plaque_marine'
print('How to access a certain attribute')
print(f"{df.loc[fighter, 'Name']} is fighting with{df.loc[fighter, '[Weapons]']}\n")

print("Missing attribute issue")
for i in df.index:
    print(f"{df.loc[i, 'Name']:25}  Quantity = {df.loc[i, 'Quantity']}")
