from tabulate import tabulate

customers_list = [["Imię", "Nazwisko"], ["Sebastian", "Kondracki"], ["Jan", "Nowak"]]
print(tabulate(customers_list, headers="firstrow", tablefmt="pretty"))