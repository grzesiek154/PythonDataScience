with open("customers.txt", "r+") as txt_file:
    print("Zawartość pliku customers.txt")
    lines = txt_file.read().strip()
    customers = lines.split("\n")
    
    for customer in customers:
        print(customer)