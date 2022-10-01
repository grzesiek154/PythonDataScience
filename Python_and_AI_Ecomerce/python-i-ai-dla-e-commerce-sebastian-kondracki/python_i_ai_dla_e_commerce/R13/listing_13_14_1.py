import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.pipeline import Pipeline
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report

class CustomImputer(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()
        self.age_means = {}
    def fit(self, X, y=None):
        self.age_means = X.groupby(["occupation"]).age.mean()
        return self
    def transform(self, X, y=None):
        X.loc[(X["age"] > 67) & (X["occupation"] == "UNKOWN"), "occupation"] = "RETIRED"
        X.loc[(X["age"] < 25) & (X["occupation"] == "UNKOWN"), "occupation"] = "STUDENT"
        for key, value in self.age_means.items():
            X.loc[((np.isnan(X["age"])) & (X.occupation == key[0])), "age"] = value
        return X

url = "https://zazepa.pl/download/datasets/customer_churn3010.csv"
df = pd.read_csv(url)
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("category")
df = df.dropna(subset=["days"])
df["resignation"] = LabelEncoder().fit_transform(df["resignation"].values)
y = df["resignation"]
X = df[df.columns.difference(["resignation"])]
imputer = Pipeline(steps=[("custom_imputer", CustomImputer())])
numeric_features = ["days"]
numeric_transformer = StandardScaler()
categorical_features = ["occupation", "reminder", "subscription"]
categorical_transformer = OneHotEncoder(handle_unknown="ignore")
preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)
pipeline = Pipeline(
    steps=[
        ("first_imputer", imputer),
        ("preprocessor", preprocessor),
        ("classifier", LinearSVC()),
]
      )
X_train, X_test, y_train, y_test = train_test_split(X, y)
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
print(y_pred)
print("model score: %.3f" % pipeline.score(X_test, y_test))

unique_label = np.unique([y_test, y_pred])
df_cm = pd.DataFrame(
    confusion_matrix(y_pred, y_test, labels=unique_label),
    index=["predykcja:{:}".format(x) for x in unique_label],
    columns=["stan faktyczny:{:}".format(x) for x in unique_label],
)
print(df_cm)
cr = classification_report(y_test, y_pred)
print(cr)