import pandas as pd

df = pd.DataFrame(
    [["2021-01-01", 1200.00], ["2021-01-02", 3200.00], ["2021-01-03", 1800.00]],
    columns=["day", "income"],
)

print(df)
df = df.set_index(["day"])
print(df)
