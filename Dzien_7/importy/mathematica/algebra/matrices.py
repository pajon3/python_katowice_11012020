def add_matrices(m1, m2):
    result = []
    row = []
    for row_i in range(len(m1)):
        for col_i in range(len(m1[0])):
            row.append(m1[row_i][col_i] + m2[row_i][col_i])
        result.append(row)
        row = []
    return result


def sub_matrices(m1, m2):
    result = []
    row = []
    for row_a, row_b in zip(m1,m2):
        row = []
        for col_a, col_b in zip(row_a, row_b):
            row.append(col_a-col_b)
        result.append(row)

    return result
