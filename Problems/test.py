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
        print(f'p: {p} sum:{s} answer: {s} diff: {s-a}')
    pass


def test2():
    print(f'n > {log2(0.5)/log2(0.99)}')

    b = 0
    for i in range(3):
        b += binom.pmf(21+i, 23, 0.75)
    print(binom.pmf(17, 17, 0.75) + binom.pmf(16, 17, 0.75))
    print(b)


def test3():
    n = 23
    p = 0.75
    m = (n + 1) * p
    print(f'(n+1)p: {int(m)} {binom.pmf(int(m), n, p)} {binom.pmf(int(m)-1, n, p)} {binom.pmf(int(m)+1, n, p)}')


def test4():
    n = 500
    p = 1/365
    lam = n * p
    for k in range(6):
        bino = binom.pmf(k+1, n, p)
        po = poisson.pmf(k+1, lam)
        print(f'binomial: {bino:.5} poisson: {po:.5} diff: {abs(bino-po):.5}')


if __name__ == '__main__':
    test_funcs = [test4]
    for test in test_funcs:
        test()
