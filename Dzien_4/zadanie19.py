def select(lista, f):

    result= []
    for i in lista:
        if f(i) :
            result.append(i)
    return result


def test_select():
    assert select([1,3,8,12,9,4,16], lambda x: x%2  == 0) == [8,12,4,16]
    assert select([1, 3, 8, 12, 9, 4, 16], lambda x: x > 10 ) == [12,16]
