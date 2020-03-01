from mathematica.geometry.figures import square_area, triangle_area



def test_square_area():
    assert square_area(4) == 16
def test_trianggle_area():
    assert triangle_area(4,4) == 8
