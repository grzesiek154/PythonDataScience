import re
names = ["Sebastian", "Seweryn", "Anna", "Wojciech"]
pattern = re.compile("Se")
for name in names:
    match = re.search(pattern, name)
    if match:
        print("Wzorzec wykryty w tekście", name)
        print(match.start())
        print(match.end())
        print(match.span())
        print(match.pos)
        print(match.endpos)
        print(match)
    else:
        print("Wzorzec nie wykryty w tekście", name)
