
def capital_indexes(string):
    result= []
    i= 0
    for letter in string:
        if letter.isupper() == True:
            result.append(i)
        i += 1
    return result


def test_capital_indexes():
    assert capital_indexes("HeLLo")== [0,2,3]