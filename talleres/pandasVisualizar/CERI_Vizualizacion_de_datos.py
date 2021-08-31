"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd

data = pd.read_csv('MovilizacionSalienteCERI.csv')
print (data.columns)

#Limpieza de datos NAN
data['Presupuesto asignado'] = data['Presupuesto asignado'].fillna(0)

#Grafica plot
