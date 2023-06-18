# https://contest.yandex.ru/contest/50252/problems/C/
# В данной задаче вы должны реализовать поиск расстояния Левенштейна между строками.
# В первой строке число n (1≤n≤10^6) - количество пар строк, которые надо сравнить и вычислить расстояния Левенштейна.
# Затем идут 2⋅n строк si (0≤∣si∣≤4000), которые и надо сравнить попарно. Смотрите примеры для лучшего понимания.
# На выходе - одна строка, в которой n чисел, разделенных пробелами, каждое число - это минимальное расстояние
# Левенштейна для пары строк. Расстояния должны соответствовать порядку пар строк для сравнения на входе (1-е число -
# расстояние для 1-й пары, 2-е число - расстояние для 2-й пары...).

def lev(s1, s2):
    n1 = len(s1) + 1
    n2 = len(s2) + 1
    dp = [[0] * n2 for _ in range(n1)]

    for i in range(1, n1):
        dp[i][0] = i
    for j in range(1, n2):
        dp[0][j] = j

    for i in range(1, n1):
        for j in range(1, n2):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1], dp[i][j - 1]) + 1
    return dp[-1][-1]


def test0():
    test_data = ((('sunday', 'saturday'), ('sunday', 'sudnay')),
                 (('sunday', 'saturday'), ('cat', 'cats'), ('cats', 'cat')))
    for pairs in test_data:
        print(*[lev(s1, s2) for s1, s2 in pairs])


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()

