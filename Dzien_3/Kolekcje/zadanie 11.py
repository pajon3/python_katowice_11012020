zbior = set()
parzyste = set(range(0,101,2))
liczba =0
while True:
    liczba = input("wprowadźliczbę lub k żeby zakończyć")
    if liczba == "k":
        break
    zbior.add(int(liczba))
print(zbior)
print(parzyste)

print(zbior & parzyste)
