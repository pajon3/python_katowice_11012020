liczba_min = None
liczba_max = None

while True:
    liczba  = (input("Wprowadź liczbę: "))
    if liczba == "koniec":
        break
    if liczba_min == None:
        liczba_min = (liczba)
        liczba_max = (liczba)

    if liczba < liczba_min:
        liczba_min = liczba
    if liczba > liczba_max:
        liczba_max = liczba
if liczba_min is None:
    print("Nie wprowadzono żadnej wartości")
else:
    print("Maksimum: ", liczba_min)
    print("Minimum: "liczba_max)