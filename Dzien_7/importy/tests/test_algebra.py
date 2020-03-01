from mathematica.algebra.matrices import add_matrices, sub_matrices

a = [[1, 2], [3, 4]]
b = [[5, 6], [7, 8]]




def test_add_matrices():
    assert add_matrices(a, b) == [[6, 8], [10, 12]]


def test_sub_matrices():
    assert sub_matrices(b, a) == [[4, 4], [4, 4]]
