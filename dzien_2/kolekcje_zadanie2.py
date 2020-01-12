lista = []

while len(lista) < 10:
    nowa_liczba = input("Wprowadź liczbę: ")
    if nowa_liczba == "k":
        break
    try:
        nowa_liczba = int(nowa_liczba)
        lista.append(nowa_liczba)
    except ValueError:
        print("No przecież liczbę masz wpisać")
    print(lista)
print(sum(lista)/len(lista))
