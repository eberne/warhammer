import pandas as pd

models = pd.read_csv('model_data.csv')
models.rename(index={0: 'plaque_marine',
                     1: 'plaque_marine_champion',
                     2: 'plaque_marine_gunner',
                     3: 'intercessor',
                     4: 'intercessor_sergeant',
                     5: 'guardsman',
                     6: 'guardsman_sargent'},
              inplace=True)

models["Quantity"] = models['Quantity'].fillna(-1)  # in order to get astype to work
models['Quantity'] = models['Quantity'].astype(int)  # Not sure why this is necessary

fighter = 'plaque_marine'
print('How to access a certain attribute')
print(f"{models.loc[fighter, 'Name']} is fighting with{models.loc[fighter, '[Weapons]']}\n")

print("Missing attribute issue")
for i in models.index:
    print(f"{models.loc[i, 'Name']:25}  Quantity = {models.loc[i, 'Quantity']}")

models = models.T
print("\n\n")
print(models.head())
