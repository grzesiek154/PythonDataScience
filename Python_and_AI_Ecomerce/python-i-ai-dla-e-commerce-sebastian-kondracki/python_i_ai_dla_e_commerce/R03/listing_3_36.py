try:
    a = int("a")
    b = 0
    c = a / b
except ValueError:
    c = None
    print("Wystąpił błąd konwersji")
except ZeroDivisionError:
    c = None
    print("Wystąpił błąd dzielenia przez zero")
except:
    c = None
    print("Błąd typu:")

print(c)
