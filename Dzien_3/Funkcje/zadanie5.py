def only_inits(a,b):
    if  type(a) == int and type(b) == int:
        return True
    return False


def test_only_ints_integers():
    assert only_inits(1,2) == True
def test_only_ints_integers():
    assert only_inits("a",1) == False
def test_only_ints_integers():
    assert only_inits(1,True) == False
