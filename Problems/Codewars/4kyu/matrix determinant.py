# https://www.codewars.com/kata/52a382ee44408cea2500074c

def minor(matrix, k):
    return [[row[j] for j in range(len(matrix)) if j != k] for i, row in enumerate(matrix) if i != 0]


def determinant(matrix):
    n = len(matrix)
    if n == 1:
        return matrix[0][0]
    if n == 2:
        return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    det = 0
    for i in range(n):
        det += matrix[0][i] * determinant(minor(matrix, i)) * (1 - 2 * (i % 2))

    return det


def test0():
    m1 = [[4, 6], [3, 8]]
    m5 = [[2, 4, 2], [3, 1, 1], [1, 2, 0]]
    print(determinant(m1))
    print(determinant(m5))


def test1():
    m2 = [[6, 1, 1], [4, -2, 5], [2, 8, 7]]
    m2a = [[2, 4, -3], [1, 8, 7], [2, 3, 5]]
    m3 = [[1, 2, 3, 4], [5, 0, 2, 8], [3, 5, 6, 7], [2, 5, 3, 1]]
    m4 = [[2, 5, 3, 6, 3], [17, 5, 7, 4, 2], [7, 8, 5, 3, 2], [9, 4, -6, 8, 3], [2, -5, 7, 4, 2]]
    m6 = [[1, 2, 4, 0, 9], [2, 3, 4, 1, 1], [6, 7, 3, 9, 3], [2, 0, 3, 0, 2], [4, 5, 2, 3, 1]]
    m7 = [[2, 4, 5, 3, 1, 2], [2, 4, 7, 5, 3, 2], [1, 1, 0, 2, 3, 1], [1, 3, 9, 0, 3, 2], [1, 1, 2, 2, 4, 1],
          [0, 0, 4, 1, 2, 3]]
    m8 = [[3, 2, 1, 4, 0, 1], [1, 2, 3, 1, 9, 1], [0, 2, 1, 1, 9, 0], [8, 2, 1, 0, 2, 3], [2, 3, 4, 0, 1, 2],
          [2, 1, 0, 0, 1, 1]]

    ms = [m2, m2a, m3, m4, m6, m7, m8]
    rs = [-306, 113, 24, 2060, 1328, 88, -536]
    for m, r in zip(ms, rs):
        assert determinant(m) == r


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
