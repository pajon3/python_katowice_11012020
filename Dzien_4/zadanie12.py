
def largest_difference(lista):
    return max(lista)-min(lista)


def largest_difference2(*liczby):
    return max(liczby)-min(liczby)



def test_largest_difference():
    assert largest_difference([1,2,3,10]) == 9

def test_largest_difference2():
    assert largest_difference2(1,2,3,10,25) == 24