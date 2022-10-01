import pandas as pd
url = "https://zazepa.pl/download/datasets/emails.csv"
df = pd.read_csv(url)
print("Liczba wiadomości",df.shape[0])
print("Liczba etykiet", df['category'].nunique())
print(df['category'].unique())