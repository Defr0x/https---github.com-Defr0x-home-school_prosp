import pandas as pd


data=pd.read_csv("wine.csv")
print(data[(data.price>20) & (data.country == "US")])
