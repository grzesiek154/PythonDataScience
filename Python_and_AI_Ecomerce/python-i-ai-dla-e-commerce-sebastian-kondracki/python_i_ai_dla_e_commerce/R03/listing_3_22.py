from tabulate import tabulate

customers_list = [["Imię", "Nazwisko"], ["Sebastian", "Kondracki"], ["Jan", "Nowak"]]
customers_dict = {"Imię": ["Sebastian", "Jan"], "Nazwisko": ["Kondracki", "Nowak"]}

print(tabulate(customers_list, headers="firstrow"))
print(tabulate(customers_dict, headers="keys"))