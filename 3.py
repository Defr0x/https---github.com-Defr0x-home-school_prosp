import pandas as pd


data=pd.read_csv("wine.csv")
print(data.dropna(how="all"))
