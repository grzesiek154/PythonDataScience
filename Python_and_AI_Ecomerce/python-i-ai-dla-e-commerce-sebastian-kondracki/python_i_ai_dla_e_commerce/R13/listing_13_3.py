import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns

url = "https://zazepa.pl/download/datasets/customer_churn3010.csv"
df = pd.read_csv(url)

for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("category")

df = df.dropna(subset = ['days'])
df["age"] = df.groupby("occupation")["age"].apply(lambda x:
x.fillna(x.mean()))
df.loc[(df['age'] > 67) & (df['occupation']=='UNKOWN'), 'occupation'] = 'RETIRED'
df.loc[(df['age'] < 25) & (df['occupation']=='UNKOWN'), 'occupation'] = 'STUDENT'

imputer = SimpleImputer(missing_values='UNKOWN', strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns, index=df.index)
df_imputed = df_imputed.astype(df.dtypes.to_dict())
df_imputed["resignation"] = LabelEncoder().fit_transform(df_imputed["resignation"].values)

for col in ["reminder", "subscription", "occupation", "gender"]:
    resignation_yes = df_imputed[df_imputed["resignation"] == 1][col].value_counts()
    resignation_no = df_imputed[df_imputed["resignation"] == 0][col].value_counts()
    df_resignation_yes_no = pd.DataFrame([resignation_yes, resignation_no])
    df_resignation_yes_no.index = ["C:YES", "C:NO"]
    df_resignation_yes_no.plot(kind="bar", stacked=True, title = col)
    plt.show()