customers = ["Kowalski", "Nowak", "Wiśniewski", "Kowalczyk","Józefowicz"]

print("Początkowa lista: ", customers)
del customers[2]
print("Lista z usuniętym drugim elementem: ", customers)
print("Funkcja pop zwraca ostatni element i usuwa go: ",customers.pop())
customers.remove('Kowalczyk')
print("Lista po usunięciu Kowalczyka: ", customers)
print("Ostateczna wielkość listy: ", len(customers))