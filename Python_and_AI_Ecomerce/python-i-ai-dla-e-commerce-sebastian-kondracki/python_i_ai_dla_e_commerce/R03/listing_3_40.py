txt_file = open("customers.txt", "r+")
print("Zawartość pliku customers.txt")
print(txt_file.read().strip())
txt_file.close()