
def is_anagram(a,b):

    a = a.lower()
    b = b.lower()
    a = sorted(a)
    b = sorted(b)
    if a == b:
        return True
    else:
        return False


def test_is_anagram():
    assert is_anagram("Tokio", "Kioto") == True
    assert is_anagram("Petersburg", "Moskwa") == False