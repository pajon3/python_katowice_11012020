

def anagram(a, b):

    return sorted(a.upper()) == sorted(b.upper())

def test_anagram():
    assert anagram("Tokio", "Kioto") is True
