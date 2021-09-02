import pandas as pd
import numpy as np


a = np.random.randint(low=0, high=10, size=(5,5))
df = pd.dataframe(data=a, columns=["A","B","C","D","E"])

print(df)

print("--------------------")

print(df.agg(('sun','mean','median','std','product')))
