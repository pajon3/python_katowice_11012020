
def double_letters(string):
    x = len(string)
    result = False

    for i in range(0, x-1):
        if string[i] == string[i+1]:
            result = True
            break
    return result


def test_double_letters():
    assert double_letters('ala') is False
    assert double_letters('aanawal') is True
    assert double_letters('nono') is False