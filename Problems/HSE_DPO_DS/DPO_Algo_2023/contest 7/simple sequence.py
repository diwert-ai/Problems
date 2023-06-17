# https://contest.yandex.ru/contest/50168/problems/B/
# Вычислите n-й член последовательности, заданной формулами:
# a2n = an + an-1,
# a2n+1 = an - an-1,
# a0 = 1, a1 = 1.
# Вводится натуральное число n, не превосходящее 1000.

def answer(n):
    a = [1] * 1002

    for i in range(1, n // 2 + 1):
        a[2 * i] = a[i] + a[i - 1]
        a[2 * i + 1] = a[i] - a[i - 1]

    return a[n]


def test0():
    test_data = [1, 2, 3, 4, 999, 1000]
    for n in test_data:
        print(answer(n))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
