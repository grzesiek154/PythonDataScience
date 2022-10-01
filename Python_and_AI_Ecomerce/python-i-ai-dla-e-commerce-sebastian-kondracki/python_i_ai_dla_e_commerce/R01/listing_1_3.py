from tabulate import tabulate
customers = []
customers.append(["Anna", "Nowak"])
customers.append(["Jan", "Kowalski"])
print(tabulate(customers, headers=["Imię", "Nazwisko"]))
