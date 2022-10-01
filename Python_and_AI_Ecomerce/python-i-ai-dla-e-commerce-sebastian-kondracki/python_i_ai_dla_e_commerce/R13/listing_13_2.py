import pandas as pd
from sklearn.impute import SimpleImputer

url = "https://zazepa.pl/download/datasets/customer_churn3010.csv"
df = pd.read_csv(url)
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("category")
        
df = df.dropna(subset = ['days'])
df["age"] = df.groupby("occupation")["age"].apply(lambda x: x.fillna(x.mean()))
df.loc[(df['age'] > 67) & (df['occupation']=='UNKOWN'), 'occupation'] = 'RETIRED'
df.loc[(df['age'] < 25) & (df['occupation']=='UNKOWN'), 'occupation'] = 'STUDENT'
imputer = SimpleImputer(missing_values="UNKOWN",
strategy="most_frequent")
df["occupation"] = imputer.fit_transform(df[["occupation"]]).ravel()
print(df.isnull().any())
print(df.groupby("occupation")["occupation"].size())