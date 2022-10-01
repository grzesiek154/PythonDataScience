txt_file = open("customers.txt", "w")
lines = ["Jan Nowak", "Anna Kowalska", "Sebastian Kowalczyk"]
txt_file.write("Klienci:" + "\n")
txt_file.writelines("%s\n" % l for l in lines)
txt_file.close()
