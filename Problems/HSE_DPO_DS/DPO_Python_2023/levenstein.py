def levenstein(a, b):
    n, m = len(a) + 1, len(b) + 1
    f = [[i + j if i == 0 or j == 0 else 0 for j in range(m)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1])

    return f[-1][-1]


def test0():
    tests = (('horse', 'rorse'),
             ('bug', 'bag'),
             ('hug', 'hat'),
             ('cat', 'bug'),
             ('mud', 'moody'))
    for a, b in tests:
        print(f'{a}->{b}: {levenstein(a, b)}')


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
