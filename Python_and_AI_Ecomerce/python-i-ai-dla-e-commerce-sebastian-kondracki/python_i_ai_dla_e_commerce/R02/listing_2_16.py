returning_customer = set()
returning_customer.add("Maślanki")
returning_customer.add("Mleko")
returning_customer.add("Napoje alkoholowe")
returning_customer.add("Soki")
returning_customer.add("Wody")
returning_customer.add("Wędliny")
returning_customer.add("Kawy")

if "Soki" in returning_customer:
    print("Kategoria 'Soki' znajduje się w zbiorze")

for category in returning_customer:
    print("Iteracja: ", category)

print("Wybranie losowego elementu i usunięcie go: ",
returning_customer.pop())
returning_customer.discard("MP3")
returning_customer.remove("Kawy")
print(returning_customer)