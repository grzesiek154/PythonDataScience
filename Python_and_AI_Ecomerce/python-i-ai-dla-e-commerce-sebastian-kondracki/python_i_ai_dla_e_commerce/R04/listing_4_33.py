import pandas as pd
import numpy as np

df = pd.read_csv("bank-full.csv", sep=";")
df['age'] = df['age'].astype('float64')
object_columns = list(df.select_dtypes(include="object"))
df[object_columns] = df[object_columns].astype(pd.StringDtype())
df.loc[df.sample(frac=0.4).index, "age"] = np.nan

if df["age"].isnull().values.any():
    print(df["age"].isnull().sum())
    print(df["age"].describe().T)
    df["age"] = df["age"].fillna((df["age"].mean()))
    print(df["age"].isnull().sum())
    print(df["age"].describe().T)