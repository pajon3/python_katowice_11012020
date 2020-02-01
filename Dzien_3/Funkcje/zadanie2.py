def test_mid_without_middle_letter():
    assert(mid("aabbcc")) ==""

def test_mid_with_middle_letter():
    assert(mid("abbcc")) =="b"
def test_mid_empty_string():
    assert(mid("abbcc")) ==""



def mid(napis):
    x = len(str(napis))
    if x % 2 == 0 or x == 0:
        sr = ""
    else:
        sr =napis[int(x/2)]
    return sr
