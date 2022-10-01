import pandas as pd

df = pd.read_csv("bank-full.csv",sep=';')
print(df.info())
print(df.describe())