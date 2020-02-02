import string
def palindrom(napis):
    # napis = napis.lower()
    # napis_nowy = ""
    # for l in napis:
    #     if l != " " and l !=",":
    #         napis_nowy += l
    #
    # x = len(napis_nowy)
    #
    # for i in range(0,x):
    #     if napis_nowy[i] == napis_nowy[x-i-1]:
    #         result = True
    #     else:
    #         result = False
    #         break
    # return result




    napis = napis.lower()
    for s in string.punctuation +string.whitespace:
        napis = napis.replace(s,"")
    return napis == napis[::-1]



def test_palindrom():
    assert palindrom("kajak") is True
    assert palindrom("kajsk") is False
    assert palindrom("Ile Romanowi dała za ład Iwona moreli") is True