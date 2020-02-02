
def div(a:int, b: int= 2):

    if a & b == 0:
        return True
    else:
        return False


def test_div():
    div(10,5) is True
    div (10,3) is False
    div(10) is True
