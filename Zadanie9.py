import datetime

akt_rok =datetime.datetime.now().year


rok = int(input("Podaj datę urodzenia :"))

wiek = akt_rok-rok


if  wiek<18:
    print(f"Masz {wiek} lat. Jesteś niepełnoletni")
else:
    print(f"Masz {wiek} lat. Jesteś pełnoletni")
