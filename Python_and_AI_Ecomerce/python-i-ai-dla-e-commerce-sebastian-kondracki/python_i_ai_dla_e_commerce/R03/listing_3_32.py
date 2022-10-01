customers = ["Sebastian", "Jan", "Henryk", "Agnieszka", "Anna"]
women = [first_name for first_name in customers if first_name[-1] == "a"]
print(women)