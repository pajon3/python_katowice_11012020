# #Napisz funkcję o nazwie capital_letters, która
# Przyjmie 1 argument - napis
# zwróci indeksy wielkich liter

def capital_letters(napis):
    indeksy = []
    for l in range(0,len(napis)):
        if napis[l].isupper() == True:
            indeksy.append(l)
    return  indeksy




def test_capital_letters_small_and_big_letters():
    assert capital_letters("HeLlO") == [0,2,4]
def test_capital_letters_small_and_big_letters():
    assert capital_letters("heLlo") == []



