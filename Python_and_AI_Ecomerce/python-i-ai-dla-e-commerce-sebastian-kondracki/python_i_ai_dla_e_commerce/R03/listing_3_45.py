import time
      
start = time.time()
count = 0
found = 0
with open("en-books-dataset.csv", encoding="UTF-8") as file:
    for line in file:
        if "Clostridium tetani" in line:
            found = found + 1
        count = count + 1
end = time.time()

print("Czas wyszukiwania [s]: ", (end - start))
print("Liczba linii: ", count)
print("Wynik: ", found)