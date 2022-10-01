days = ("poniedziałek", "wtorek", "środa", "czwartek", "piątek", "sobota", "niedziela")
print(days)
print("Pierwszy element, czyli ten o indeksie 0: ", days[0])
print("Ostatni element: ", days[len(days)-1])
print("Ostatni element (alternatywnie): ", days[-1])
for day in days:
    print("Iteracja: ", days.index(day), day)