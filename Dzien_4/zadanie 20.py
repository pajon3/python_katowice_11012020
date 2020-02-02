
def przytnij(data, start, stop):
    tabela = []
    for numer in data:
        if stop(numer):
            tabela.append(numer)
            break
        if start(numer):
            tabela.append(numer)
    return tabela

def test_przytnij():
    assert przytnij(
        [1,2,3,4,2,5,6,7],
        lambda x: x>3,
        lambda x: x == 6
    ) == [4,5,6]