import scipy as sp
import numpy as np
from math import log2
from scipy.stats import binom, poisson


def entropy(a):
    return -sum(map(lambda x: x * log2(x) if x else 0, a))


def test0():
    a1 = [0.333, 0.333, 0.333]
    a2 = [0.3, 0.3, 0.4]
    print(f'a1 entropy: {entropy(a1)}')
    print(f'a2 entropy: {entropy(a2)}')
    pass


def answer(p):
    return (2 * p ** 2) / ((2 - p) ** 3)


def summation(p, k=10):
    s = 0
    for i in range(k):
        s += (p ** i / 2 ** i) * ((i - 1) * i / 2)

    return s


def test1():
    tests = [(0.7, 100), (0.8, 1000), (0.245, 1000), (0.111, 10)]
    for p, k in tests:
        s = summation(p, k)
        a = answer(p)
        print(f'p: {p} sum:{s} answer: {s} diff: {s - a}')
    pass


def test2():
    print(f'n > {log2(0.5) / log2(0.99)}')

    b = 0
    for i in range(3):
        b += binom.pmf(21 + i, 23, 0.75)
    print(binom.pmf(17, 17, 0.75) + binom.pmf(16, 17, 0.75))
    print(b)


def test3():
    n = 23
    p = 0.75
    m = (n + 1) * p
    print(f'(n+1)p: {int(m)} {binom.pmf(int(m), n, p)} {binom.pmf(int(m) - 1, n, p)} {binom.pmf(int(m) + 1, n, p)}')


def test4():
    n = 500
    p = 1 / 365
    lam = n * p
    for k in range(6):
        bino = binom.pmf(k, n, p)
        po = poisson.pmf(k, lam)
        print(f'k:{k} binomial: {bino:.5f} poisson: {po:.5f} diff: {abs(bino - po):.5f}')


def test5():
    print(binom.pmf(3, 6, 0.5))


def test6():
    a = np.array([[2, -1, 2], [-1, 2, -1], [1, -1, 2]])
    b = a
    for i in range(10):
        print(b)
        b = b * a


def test7():
    b = 0
    for i in range(3):
        b += binom.pmf(i, 102, 0.015)
    print(b)


def test8():
    a = [3, 4, 4, 3, 4, 3, 3, 3, 3, 3, 4, 4, 3, 3, 3, 4, 3, 3, 3, 4, 3, 5, 5, 3, 5, 4, 4, 4, 4, 5,
         3, 5, 5, 4, 5]
    print(len(a), a.count(3), a.count(4), a.count(5),
          sum(a)/len(a))


def test9():
    p = (36 * 37 * 38 * 39) / (49 * 50 * 51 * 52)
    print(binom.pmf(3, 3, p))


def test10():
    print(log2(0.1)/log2(0.9))


def test11():
    p = 4*(10 * 11 * 12 * 13) / (49 * 50 * 51 * 52)
    print(-1 / log2(1-p))


def test12():
    p = 1 / 5
    n = 10
    h = 1 - binom.pmf(0, n, p)
    ah = h - binom.pmf(1, n, p)
    print(ah/h)


def test13():
    p1 = binom.pmf(2, 13, 0.5)
    p2 = sp.special.comb(26, 2) * sp.special.comb(26, 11) / sp.special.comb(52, 13)
    print(p1, p2)


if __name__ == '__main__':
    test_funcs = [test13]
    for test in test_funcs:
        test()
