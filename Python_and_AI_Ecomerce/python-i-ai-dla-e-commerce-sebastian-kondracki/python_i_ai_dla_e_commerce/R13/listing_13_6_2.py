import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.impute import SimpleImputer
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_selection import SelectKBest, chi2
from sklearn.preprocessing import OrdinalEncoder

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

df["age"] = df.groupby("occupation")["age"].apply(lambda x: x.fillna(x.mean()))
df.loc[(df['age'] > 67) & (df['occupation']=='UNKOWN'), 'occupation'] = 'RETIRED'
df.loc[(df['age'] < 25) & (df['occupation']=='UNKOWN'), 'occupation'] = 'STUDENT'

imputer = SimpleImputer(missing_values='UNKOWN', strategy='most_frequent')
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns, index=df.index)
df_imputed = df_imputed.astype(df.dtypes.to_dict())
df_imputed["resignation"] = LabelEncoder().fit_transform(df_imputed["resignation"].values)

for col in ["age", "days"]:
    sns.kdeplot (df_imputed[col].loc[df_imputed["resignation"] == 1], shade = True, color = "red")
    sns.kdeplot (df_imputed[col].loc[df_imputed["resignation"] == 0], shade = True, color = "green")
    plt.show()


df_encoded = df_imputed[["gender", "occupation", "reminder", "subscription", "resignation"]].copy()
label_encoder = LabelEncoder()
df_encoded["resignation"] = LabelEncoder().fit_transform(df_encoded["resignation"])
category_encoder = OrdinalEncoder()
df_encoded[df_encoded.columns.difference(["resignation"])] = category_encoder.fit_transform(df_encoded[df_encoded.columns.difference(["resignation"])])
y = df_encoded["resignation"]
X = df_encoded[["gender", "occupation", "reminder", "subscription"]]
selector = SelectKBest(score_func=chi2, k="all")
feature_rank = selector.fit(X, y)
df_feature_rank = pd.DataFrame(data=feature_rank.scores_, index=X.columns, columns=["score"])
print(df_feature_rank.to_string(formatters={"score": "{:f}".format}))


