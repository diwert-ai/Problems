# https://contest.yandex.ru/contest/50168/problems/K/
# Дан набор гирек массой m1, …, mN. Можно ли их разложить на две чаши весов, чтобы они оказались в равновесии?
# Первая строка входных данных содержит натуральное число N, не превышающее 100. Далее идет N натуральных чисел mi, не
# превышающих 100.
# Программа должна вывести YES, если гирьки можно разложить на две кучки равной массы или NO в противном случае.

def answer(array):
    n = len(array)
    s = sum(array)
    if s % 2:
        return 'NO'
    else:
        m = s // 2
        dp = [[-1] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1, n+1):
            wi = array[i]
            for j in range(m+1):
                dp[i][j] = dp[i-1][j]
                if j - wi >= 0 and dp[i-1][j - wi] != -1:
                    dp[i][j] = 1

            if dp[i][-1] != -1:
                return 'YES'

        return 'NO'


def test0():
    test_data = ([4, 2, 3, 1], [17], [19, 19])
    for array in test_data:
        print(answer([0]+array))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
