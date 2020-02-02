
def consecutive(text):
    seria = 0
    seria_max = 0
    for i in range(0,len(text)-1):
        if text[i] == text[i+1]:
            seria +=1
            seria_max = max(seria, seria_max)
        else:
            seria = 0
    return seria_max+1



def test_consecutive():
    assert consecutive("aabbbbaabbbbbababba") == 5
    assert consecutive("ddddiddd") == 4
    assert consecutive("rrrtrrrtrrr") == 3
    assert consecutive("eererewwerewww") == 3
    assert consecutive("eeeeer") == 5