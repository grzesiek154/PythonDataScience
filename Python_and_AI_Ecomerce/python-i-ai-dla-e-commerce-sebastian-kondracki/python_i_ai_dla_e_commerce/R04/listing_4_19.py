import pandas as pd

df = pd.DataFrame(
    [
        ["Jan", "Maria", "Julian"],
        ["Kowalski", "Nowak", "Wielki"],
        [12000, 5000, 10000],
    ],
    index=[1, 2, 3],
    columns=["first_name", "last_name", "income"],
)

print(df)
