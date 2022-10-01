import pandas as pd


df = pd.DataFrame(
    [["2021-01-01", 1200.00], ["2021-01-02", 3200.00], ["2021-01-03", 1800.00]],
    columns=["day", "income"],
)

print("Wybór wartości za pomocą iat:", df.iat[1, 1])
print("Wybór wartości za pomocą iloc:", df.iloc[1, 1])
df = df.set_index(["day"])
print("Wybór wartości za pomocą at:", df.at["2021-01-02", "income"])
print("Wybór wartości za pomocą loc:", df.loc["2021-01-02", "income"])
