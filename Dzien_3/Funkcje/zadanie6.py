
def double_letters(napis):

    x = len(napis)-1
    for i in range(1,x):
        if napis[i] == napis[i+1]:
            return True
            break
        else:
            return  False

def test_double_letters_warianty():
    assert double_letters("ala") == False
def test_double_letters_wariantyy():
    assert double_letters("alla") == True
def test_double_letters_wariantyyy():
    assert double_letters("nono") == False