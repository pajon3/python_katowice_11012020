cennik = {"Jabłka": 3,
          "Banany": 4.20,
          "Gruszki": 4.50,
          "Brzoskwinie": 2.30}
magazyn = {"Jabłka": 50,
           "Banany": 43.2,
           "Gruszki": 20,
           "Brzoskwinie": 14}

while True:

    osoba = input("klient czy magazynier? ")


    if osoba == "magazynier":

        towar = input("Jaki towar przywiozłeś?")
        cena = float(input("Podaj nową cenę: "))
        ilosc = float(input("Ile kg?"))
        cennik[towar] = cena
        magazyn[towar] = magazyn.get(towar,0)+ ilosc
        print(cennik)
        print(magazyn)


    elif osoba == "klient":
        print("Witaj, w naszym sklepie oferujemy: ")

        for c in cennik:
            print(f"{c} w cenie: {cennik[c]}")
        towar = input("Co chcesz kupić:  ")
        if cennik.get(towar) == None:
            print("Niestety, nie posadamy tego towaru w naszym sklepie")
        else:
            ilosc = float(input("Ile kg? "))
            # if ilosc> magazyn[towar]:                      dodać opcję zbyt małej ilości towaru
            #     print
            print(f"Koszt zakupu wynosi: {cennik.get(towar) * ilosc}")
    else:
        print("do widzenia")
        break