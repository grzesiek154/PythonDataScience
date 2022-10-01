import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report
import pickle
import os

url = "https://zazepa.pl/download/datasets/customer_churn3010.csv"
df = pd.read_csv(url)
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("category")
df = df.dropna(subset=["days"])
df["age"] = df.groupby("occupation")["age"].apply(lambda x: x.fillna(x.mean()))
df["age"] = df["age"].fillna(df["age"].mean())
df["resignation"] = LabelEncoder().fit_transform(df["resignation"].values)
y = df["resignation"]
X = df[df.columns.difference(["resignation"])]
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
clf = Pipeline(
    steps=[("preprocessor", preprocessor), ("classifier",
LogisticRegression())]
)
X_train, X_test, y_train, y_test = train_test_split(X, y)
clf.fit(X_train, y_train)
print("model score: %.3f" % clf.score(X_test, y_test))
y_pred = clf.predict(X_test)
cr = classification_report(y_test, y_pred)
print(cr)
base_dir = os.path.dirname(__file__)
with open(os.path.join(base_dir, "churn.bin"), "wb") as writer:
    pickle.dump(clf, writer)