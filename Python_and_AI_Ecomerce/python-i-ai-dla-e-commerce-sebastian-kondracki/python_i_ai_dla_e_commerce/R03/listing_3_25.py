from rich.console import Console
from rich.table import Table

customers = []
customers.append(["2021-02-01", "Jan Nowak", "2000,00 PLN"])
customers.append(["2021-02-01", "Anna Kowalska", "3999,90 PLN"])
customers.append(["2021-02-02", "Kondracki & Partner sp. z o.o.", "5000,00 PLN"])
customers.append(["2021-02-03", "Importex sp. z o.o.", "120,00 PLN"])

table = Table(title="Sprzedaż Q1-2021")
table.add_column("Data transakcji", justify="right", style="cyan", no_wrap=True)
table.add_column("Klient", style="magenta")
table.add_column("Przychód", justify="right", style="green")

for customer in customers:
    table.add_row(customer[0],customer[1],customer[2])

console = Console()
console.print(table)