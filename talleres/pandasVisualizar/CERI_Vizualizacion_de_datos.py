"""
Spyder Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import dateutil

data = pd.read_csv('Colfuturo-Seleccionados.csv')
#print (data)
labels = data["Área"].unique()
labels = np.sort(labels)
S2 = data["Área"].value_counts().sort_index(ascending=True)

#Gráfico de pie con porcentajes de áreas del datafame
plt.pie(S2, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)

###plt.legend()
plt.show()
