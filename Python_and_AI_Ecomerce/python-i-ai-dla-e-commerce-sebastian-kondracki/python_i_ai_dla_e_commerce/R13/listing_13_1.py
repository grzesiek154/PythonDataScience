import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
url = "https://zazepa.pl/download/datasets/customer_churn3010.csv"
df = pd.read_csv(url)
print(df.info())
for col in df.columns:
    if df[col].dtype == "object":
        df[col] = df[col].astype("category")
plt.subplots(figsize=(8, 8))
sns.heatmap(df.isnull(), cbar=False)
plt.show()
print(df.isnull().any())
sns.countplot(df['occupation'])
plt.show()