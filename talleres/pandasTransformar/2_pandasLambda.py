import pandas as pd

#create empty dataframe
df = pd.DataFrame()

#create columns
df['name'] = ['Andres', 'Sebastian', 'Gloria', 'Sergio', 'Cristian', 'Leidy']
df['weight'] = [57, 65, 64, 79, 67, 60]
df['height'] = [1.7, 1.67, 1.5, 1.79, 1.68, 1.55]

#view dataframe
print("\nDataFrame Original")
print(df)

#apply lambda
df['IMC'] = df.apply(lambda x: x['weight']/x['height']**2, axis=1)

#view dataframe
print("\nDataFrame Modificado")
print(df)