import pandas as pd
url = "https://zazepa.pl/download/datasets/emails_invalid.csv"
df = pd.read_csv(url)
print(df.info())
df['category'] = df['category'].astype('category')
df['subject'] = df['subject'].astype(pd.StringDtype())
df['message'] = df['message'].astype(pd.StringDtype())

df['length'] = df['subject'].str.len() + df['message'].str.len()
print(df.info())
print(df.describe())
print(df.describe(include='all'))
print(df['category'].describe())
print(df['category'].str.len().describe())
print(df.isnull().any())
df = df.dropna(subset=['category', 'message'])
print(df.head(2))
print(df.tail(2))
print(df.sample(5))