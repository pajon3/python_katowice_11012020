lista = [2,5,4,1,3]
imin = None
imax = None

for i in lista:
    if imin is None:
        imin = i
        imax = i
    else:
        if i< imin:
            imin = i
            indmin = lista.index(i)
        elif i>imax:
            imax = i
            indmax = lista.index(i)


lista[indmin], lista[indmax] = lista[indmax], lista[indmin]
print(lista)
assert lista == [2,1,4,5,3]