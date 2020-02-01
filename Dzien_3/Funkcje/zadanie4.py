# napisz funkcję random number, która nie przyjmuje argumentów a zwraca losową liczbę z przedziału 1-100
import random


def random_number():
    return random.randint(1,101)


def test_random_number_seed():
    random.seed(0)
    assert random_number() == 50