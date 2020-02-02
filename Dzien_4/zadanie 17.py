def policz_znaki(text, open = "<", close = ">"):
    counter = 0
    status = 0

    for sign in text:

        if sign == open:
            status += 1
        elif sign == close:
            status -= 1
        else:
            counter = counter +  status
    return counter

def test_policz_znaki():
    assert policz_znaki("ala ma <kota> kot ma ale") == 4
    assert policz_znaki("ala ma [kota [a kot]] ma [ale]","[","]") == 18
    assert policz_znaki("a <a<a<a>>>") == 6