import pandas as pd
from sklearn.base import BaseEstimator
from sklearn.base import TransformerMixin

class CustomTransformer(BaseEstimator, TransformerMixin):
    def __init__(self):
        super().__init__()
        self.max_len = 0
    def fit(self, X, y=None):
        self.max_len = X["first_name"].str.len().max()
        return self
    def transform(self, X, y=None):
        X["diff"] = self.max_len - X["first_name"].str.len()
        return X
        
df = pd.DataFrame(data=["Sebastian", "Jan", "Marzena"],
columns=["first_name"])
print(df)
print(CustomTransformer().fit_transform(df))