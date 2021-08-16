import pandas as pd

#create empty dataframe
df = pd.DataFrame()

#create columns
df['name'] = ['Damian', 'Sara', 'Ray', 'Sebastian', 'Andres', 'Sergio']
df['employed'] = ['Yes', 'Yes', 'No', 'Yes', 'No', 'Yes']
df['age'] = [32,29,19,19,20,21]

#view dataframe
print("DataFrame")
print(df)

#create functions
def add_persons(dataframe, nombre, trabajo, edad):
    #add a person
    df.loc[6] = [nombre, trabajo, edad]
    #return dataframe
    return dataframe

def uppercase_column_name(dataframe):
    #cap all the column headers
    dataframe.columns = dataframe.columns.str.upper()
    #return dataframe
    return dataframe

def mean_age_by_group(dataframe, col):
    #group the data by a column and return the mean age per group
    return dataframe.groupby(col).mean()
    
#create a pipeline that applies all functions
print("\nTuberia aplicada")
print(df.pipe(add_persons,nombre='Celeste', trabajo='Yes', edad=25).pipe(mean_age_by_group,col='employed').pipe(uppercase_column_name))