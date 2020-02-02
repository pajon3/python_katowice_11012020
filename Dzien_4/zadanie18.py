
def formatuj(* args, **kwargs):
    status = 0
    tekst = ""
    for a in args:
        for k,v in kwargs.items():
            klucz = "$" + k
            a= a.replace(klucz ,str(v))
        a = "\n"* status+a
        status = 1
        tekst = tekst+ a

    return tekst

def test_formatuj():
    assert formatuj("koszt $cena PLN",
                    'kwota $cena brutto',
                    cena = 10) == "koszt 10 PLN\nkwota 10 brutto"

