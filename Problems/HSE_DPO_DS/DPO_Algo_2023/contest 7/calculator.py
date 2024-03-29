# https://contest.yandex.ru/contest/50168/problems/C/
# Имеется калькулятор, который выполняет следующие операции:
#
# Умножить число X на 2.
# Умножить число X на 3.
# Прибавить к числу X единицу.
#
# Определите, какое наименьшее количество операций требуется, чтобы получить из числа 1 число N.
# В первой строке задается натуральное число N, не превосходящее 10^6.
# Выведите минимальное количество операций. Во второй строке выведите числа, последовательно получающиеся при выполнении
# операций. Первое из них должно быть равно 1, а последнее N.

def answer(n):
    dp = [0] * (n + 1)
    p = [0] * (n + 1)

    p[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1]
        p[i] = i - 1
        if not i % 2 and dp[i // 2] < dp[i]:
            dp[i] = dp[i // 2]
            p[i] = i // 2
        if not i % 3 and dp[i // 3] < dp[i]:
            dp[i] = dp[i // 3]
            p[i] = i // 3
        dp[i] += 1

    k = n
    result = [n]
    while p[k] != k:
        k = p[k]
        result.append(k)

    return dp[n], result[::-1]


def test0():
    test_data = (1, 2, 3, 4, 5, 100, 10 ** 6)
    for n in test_data:
        print(*answer(n))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
