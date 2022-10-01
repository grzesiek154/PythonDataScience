import pandas as pd
         
df = pd.read_csv("bank-full.csv", sep=";")
object_columns = list(df.select_dtypes(include = 'object'))
df[object_columns] = df[object_columns].astype(pd.StringDtype())
print(df['job'].describe())
job = df['job'].unique()
print(sorted(job))