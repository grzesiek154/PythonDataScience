import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder

eye_color = [
    "brązowe",
    "bursztynowe",
    "ciemnobrązowe",
    "niebieskie",
    "piwne",
    "szare",
    "zielone",
]
df1 = pd.DataFrame(columns=["eye_color"],
data=np.random.choice(eye_color, 100))
print(df1)
encoder = OneHotEncoder(sparse=False)
df_encoded1 = pd.DataFrame(data=encoder.fit_transform(df1), columns=encoder.get_feature_names_out())
print(df_encoded1)