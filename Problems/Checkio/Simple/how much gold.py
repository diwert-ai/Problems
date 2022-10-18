# https://py.checkio.org/ru/mission/how-much-gold/
from fractions import Fraction

METALS = ('gold', 'tin', 'iron', 'copper')


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


def checkio(alloys):
    a = [[Fraction(0)] * 4 for _ in range(4)]
    a[3][:] = [Fraction(1)] * 4
    for i, alloy in enumerate(alloys):
        spl = alloy.split('-')
        a[i][METALS.index(spl[0])], a[i][METALS.index(spl[1])] = Fraction(1), Fraction(1)
    g, g_c = [row.copy() for row in a], list(alloys.values()) + [Fraction(1)]
    for i in range(4):
        g[i][0] = g_c[i]
    return determinant(g)/determinant(a)


def test0():
    assert checkio({
        'gold-tin': Fraction(1, 2),
        'gold-iron': Fraction(1, 3),
        'gold-copper': Fraction(1, 4),
    }) == Fraction(1, 24), "1/24 of gold"
    assert checkio({
        'tin-iron': Fraction(1, 2),
        'iron-copper': Fraction(1, 2),
        'copper-tin': Fraction(1, 2),
    }) == Fraction(1, 4), "quarter"


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
