def up_down(liczba):
    return liczba - 1, liczba + 1


def test_up_down():
    assert up_down(5) == (4, 6)
    assert up_down(10) == (9, 11)
