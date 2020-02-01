lista = []
wynik = [(el, el**3) for el in range(10) if el %2 == 0]

lista = [(el/10) for el in range(11)]
print(lista)d

tupla = ()

tupla = ({(el, el**2, el**3) for el in range(-10,10,1)})
print(tupla)

slownik = {}
napisy = ["Ala", "ma", "kota", "i","kanarka"]
slownik = {(napis, len(napis)) for napis in napisy}
print(slownik)