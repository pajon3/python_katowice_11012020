def add_dots(napis):
    nowy_napis= ""
    for i in range(0,len(napis)):
        if napis[i] != ".":
           if i == len(napis)-1:
               nowy_napis += napis[i]
           else:
                nowy_napis += napis[i] +"."
    return nowy_napis


def remove_dots(napis):
    nowy_napis= ""
    for i in range(0,len(napis)):
        if napis[i] != ".":
            nowy_napis += napis[i]
    return nowy_napis




def test_add_dots_tekst_bez_kropek():
    assert add_dots("te...ks.....t") == "t.e.k.s.t"



def test_remove_dots_tekst_z_kropkami():
    assert remove_dots("t.e.k.s...t") == "tekst"

