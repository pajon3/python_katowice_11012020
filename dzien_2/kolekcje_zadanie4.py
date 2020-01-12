lista = []

for liczba in range(101):
    if liczba % 5 == 0 or liczba % 3 ==0:
        lista.append(liczba)
print(len(lista))

print("\n".join(map(str,lista)))
