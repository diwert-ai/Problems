# https://contest.yandex.ru/contest/50168/problems/L/
# Дано N предметов массой m1, …, mN и стоимостью c1, …, cN соответственно.
#
# Ими наполняют рюкзак, который выдерживает вес не более M. Какую наибольшую стоимость могут иметь предметы в рюкзаке?
# В первой строке вводится натуральное число N, не превышающее 100 и натуральное число M, не превышающее 10000.
# Во второй строке вводятся N натуральных чисел mi, не превышающих 100.
# Во третьей строке вводятся N натуральных чисел ci, не превышающих 100.
# Выведите одно целое число: наибольшую возможную стоимость рюкзака.

def answer(weights, costs, m):
    n = len(weights)
    dp = [[-1] * (m + 1) for _ in range(n)]
    dp[0][0] = 0
    for i in range(1, n):
        wi = weights[i]
        ci = costs[i]
        for j in range(m + 1):
            dp[i][j] = dp[i - 1][j]
            if j - wi >= 0 and dp[i - 1][j - wi] != -1:
                dp[i][j] = max(dp[i][j], dp[i - 1][j - wi] + ci)

    return max(dp[-1])


def test0():
    test_data = (([2, 4, 1, 2], [7, 2, 5, 1], 6),
                 ([18], [16], 597))
    for weights, costs, m in test_data:
        print(answer([0]+weights, [0]+costs, m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
