import pandas as pd

df = pd.read_csv("dataexport.csv")
print(df.columns)
print(df.values[0])
print(df[['Category1', 'Category2', 'Category3']])