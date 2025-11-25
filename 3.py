import pandas as pd


data=pd.read_csv("wine.csv")
print(data.iloc[10:20,4:6])
