def only_ints(a, b):

    if type(a) == int and type(b) == int:
        return True
    else:
        return False

def test_only_ints():
    assert only_ints(1,2) is True
    assert only_ints(1,True) is False
    assert only_ints("a", 2) is False