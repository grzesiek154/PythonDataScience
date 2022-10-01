import pandas as pd
import numpy as np
from sklearn.preprocessing import OneHotEncoder
booking_class = ["first", "economic", "business"]
df1 = pd.DataFrame(columns=["booking_class"],
data=np.random.choice(booking_class, 10))
print(df1)
encoder = OneHotEncoder(sparse=False, drop="first")
df_encoded1 = pd.DataFrame(data=encoder.fit_transform(df1),
columns=encoder.get_feature_names_out())
print(df_encoded1)
print(df_encoded1.info())