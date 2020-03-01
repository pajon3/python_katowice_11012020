import json
import csv

form = input("Wprowadź format: J - JSON, C - CSV")
slownik = {}

if form == "J":
    try:
        with open("zadanie1.json") as f:
            lista = json.load(f)
    except FileNotFoundError:
        lista = []

elif form == "C":
    try:
        with open("zadanie1.csv") as f:
            lista = csv.reader(f, delimiter=";")
    except FileNotFoundError:
        lista = []

akcja = input("Dodawanie rekordu - d, /n Wyświetlanie - w")
if akcja == "d":
    slownik["Imie"] = input("Wprowadź imię: ")
    slownik["Nazwisko"] = input("Wprowadź nazwisko: ")
    slownik["Pensja"] = float(input("Wprowadż pensję: "))
    slownik["Rok urodzenia"] = int(input("Wprowadż rok urodzenia: "))

    lista.append(slownik)
    slownik = {}

elif akcja == "w":
    print(lista)


if form == "J":
    with open("zadanie1.json", "w") as f:
        json.dump(lista, f)
elif form == "C":
    with open("zadanie1.csv", "w", newline = ""):
        writter =  csv.writer(f, delimiter = ";")
        writer.writerow

