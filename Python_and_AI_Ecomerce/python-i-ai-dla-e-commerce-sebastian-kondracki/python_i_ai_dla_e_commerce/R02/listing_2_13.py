customers = set()
customers.add('Kowalczyk')
customers.add('Kowalski')
customers.add('Kowalczyk')
customers.add('Nowak')
print(customers)

customers.update(("Józefowicz", "Michałowski", "Kowalczyk"))
print(customers)