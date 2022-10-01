customer = dict(first_name="Jan", last_name="Kowalski", pesel="05210722588", nip="7578390197")
      
if "first_name" in customer:
    print("Imię: ", customer['last_name'])

if "salary" in customer:
    print("Wynagrodzenie: ", customer['salary'])
else:
    print("Wynagrodzenie: brak danych")