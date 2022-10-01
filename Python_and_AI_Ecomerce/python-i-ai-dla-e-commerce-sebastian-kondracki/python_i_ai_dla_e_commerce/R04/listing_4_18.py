import pandas as pd

df = pd.DataFrame(
    {
        "first_name": ["Jan", "Maria", "Julian"],
        "last_name": ["Kowalski", "Nowak", "Wielki"],
        "income": [12000, 5000, 10000],
    },
    index=[1, 2, 3],
)

print(df)
