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
df1 = pd.DataFrame(columns=["eye_color"], data=np.random.choice(eye_color[1:], 100))
print(df1)
df2 = pd.DataFrame(columns=["eye_color"], data=np.random.choice(eye_color, 100))

print(df2)
encoder = OneHotEncoder(sparse=False)
encoder.fit(df1)
df_encoded1 = pd.DataFrame(data=encoder.transform(df1), columns=encoder.get_feature_names_out())
df_encoded2 = pd.DataFrame(data=encoder.transform(df2), columns=encoder.get_feature_names_out())
print(df_encoded2)
