try:
    a = int(input("Podaj a="))
    b = int(input("Podaj b="))
    c = a + b
except ValueError:
    print("Wystąpił błąd konwersji. Spróbuj jeszcze raz")
else:
    print("a + b = ", str(c))

finally:
    a = 0
    b = 0
    c = 0
    print("Koniec programu")
