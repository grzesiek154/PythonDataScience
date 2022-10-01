import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
df = pd.DataFrame(columns=["sales"],
data=np.random.randint(5,5000,size=1000))
print(df)
scaler = StandardScaler()
df_scaled1 = pd.DataFrame(data = scaler.fit_transform(df), columns =
scaler.get_feature_names_out())
print(df_scaled1)
min_max = MinMaxScaler()
df_scaled2 = pd.DataFrame(data = min_max.fit_transform(df), columns =
min_max.get_feature_names_out())
print(df_scaled2)