
def thousand_separator(liczba):
    x = len(str(liczba))
    liczba = str(liczba)
    napis = ""
    i = 0
    while 3 * (i+1) < x:
        napis =
        i +=1





def test_thousands_separator():
    assert thousand_separator(1000000) == "1,000,000"




