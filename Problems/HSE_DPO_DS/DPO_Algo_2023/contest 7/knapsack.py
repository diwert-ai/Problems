# https://contest.yandex.ru/contest/50168/problems/M/
# Найдите максимальный вес золота, который можно унести в рюкзаке вместительностью S, если есть N золотых слитков с
# заданными весами.
# В первой строке входного файла записаны два числа — S и N (1 <= S <= 10 000, 1 <= N <= 300).
# Далее следует N неотрицательных целых чисел, не превосходящих 100 000 — веса слитков.
# Выведите искомый максимальный вес.

def answer(m, weights):
    n = len(weights)
    dp = [[-1] * (m + 1) for _ in range(n+1)]
    dp[0][0] = 0
    weights = [0] + weights

    for i in range(1, n + 1):
        wi = weights[i]
        for j in range(m + 1):
            dp[i][j] = dp[i - 1][j]
            if j - wi >= 0 and dp[i - 1][j - wi] != -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - wi] + 1)

    for i in range(m, -1, -1):
        if dp[-1][i] != -1:
            return i


def test0():
    test_data = ((20, [5, 7, 12, 18]),
                 (10, [1, 4, 8]))

    for m, weights in test_data:
        print(answer(m, weights))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
