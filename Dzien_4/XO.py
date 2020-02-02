

def get_row_col(pole):
    columns = "ABC"
    rows = "123"
    col_n, row_n = list(pole)
    return rows.index(row_n), columns.index(col_n)


def test_get_row_col():
    get_row_col("A3") == (2,0)