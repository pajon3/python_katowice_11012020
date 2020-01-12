
napis = 'ala ma kotaaaayy'
samogloski = ['a','e','i','o','u','y']
liczba = 0

for litera in napis.lower():
    if litera in samogloski:
        liczba +=1
print(liczba)
