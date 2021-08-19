import pandas as pd
import math

#Definición de funciones
def cop_to_dolar(data_frame):
    data_frame *= 0.00026
    data_frame = round(data_frame,3)
    return data_frame

def cop_to_eur(data_frame):
    data_frame *= 0.00022
    data_frame = round(data_frame,3)
    return data_frame

def cop_to_libra(data_frame):
    data_frame *= 0.00019
    data_frame = round(data_frame,3)
    return data_frame

#Fuente: https://www.dane.gov.co/index.php/estadisticas-por-tema/precios-y-costos/precios-de-venta-al-publico-de-articulos-de-primera-necesidad-pvpapn
indice = ["Abril-2020","Mayo-2020","Junio-2020","Julio-2020","Agosto-2020","Septiembre-2020","Octubre-2020","Noviembre-2020","Diciembre-2020","Enero-2021","Febrero-2021","Marzo-2021"]

diccionario = {
    "Leche (1 Litro)": [3433,3500,3600,3500,3600,3500,3700,3600,3700,3700,3500,3700],
    "Arroz (1 Kg)": [4100,4095,4000,3900,3520,3320,3418,3294,3211,3233,3277,3233],
    "Azucar refinada (1 kg)" : [3340,3275,3274,3280,3217,3269,3121,3256,3157,3277,3138,3150],
    "Queso campesino (250 gramos)": [6867,7075,7800,7075,7050,7000,6900,7280,7150,7000,7243,7300]
}

#crea dataframe
precios_df = pd.DataFrame(diccionario, index=indice)

#imprime dataframe con peso en colombiano
print("[========================== PRECIO EN COP ===========================]\n")
print(precios_df)

#Imprime conversiones por medio de transform
print("\n\n[========================= CONVERSIONES ===========================]\n")
print(precios_df.transform([cop_to_dolar, cop_to_eur, cop_to_libra]))

print("\n\n[========================= MONEDAS =================]")
print("\n\t\t=================\n"+
      "\t\t|    COP ($)    |\n"+
      "\t\t|    USD (US$)  |\n"+
      "\t\t|    EUR (€)    |\n"+
      "\t\t|    Libra (£)  |\n"+
      "\t\t=================")

#Las medidas para las conversiones son del día 18 de agosto del 2020
#   -> 1 COP = 0.00026 USD
#   -> 1 COP = 0.00022 EUR
#   -> 1 COP = 0.00019 Libras (GBP)
