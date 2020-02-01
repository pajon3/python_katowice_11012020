
def count(napis):
    x = 1
    for i in napis:
        if i == "-":
            x += 1
    return x



def test_count():
    assert count("ho-tel") == 2
    assert count("ter-mi-na-tor") ==4
