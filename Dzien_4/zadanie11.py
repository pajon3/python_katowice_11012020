# Napisz funkcję, która jako argument przyjmie listę list
#  i zwróci listębędącą ich połączeniem

def flatten(a):
    lista = []
    for i in a:
        for x in i:
            lista.append(x)
    return lista


def test_flatten():
   assert flatten([[1,2],[3,4]]) == [1,2,3,4]


def flatten(*a):
    lista = []
    for i in a:
        for x in i:
            lista.append(x)
    return lista


def test_flatten():
   assert flatten([1,2],[3,4]) == [1,2,3,4]