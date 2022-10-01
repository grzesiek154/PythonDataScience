txt_file = open("customers.txt", "r+")
print("Zawartość pliku customers.txt")
lines = txt_file.read().strip()
customers = lines.split("\n")
for customer in customers:
    print(customer)
txt_file.close()