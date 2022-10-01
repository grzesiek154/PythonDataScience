customer = dict(first_name="Jan", last_name="Kowalski", pesel="05210722588", nip="7578390197")

print(customer['first_name'])
print(customer.get('last_name'))
print(customer.get('phone'))

for key in customer:
    print("Klucz: ", key)
    print("Wartość:", customer[key])