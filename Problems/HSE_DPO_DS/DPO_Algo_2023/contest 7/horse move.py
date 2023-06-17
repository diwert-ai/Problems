# https://contest.yandex.ru/contest/50168/problems/J/
# Дана прямоугольная доска N × M (N строк и M столбцов). В левом верхнем углу находится шахматный конь, которого
# необходимо переместить в правый нижний угол доски. При этом конь может ходить ТОЛЬКО на две клетки вниз и на одну
# клетку вправо, либо на две клетки вправо и на одну клетку вниз. Необходимо определить, сколько существует различных
# маршрутов, ведущих из левого верхнего в правый нижний угол.
# В первой строке входного файла находятся два натуральных числа N и M (1 ≤ N, M ≤ 50).
# В выходной файл выведите единственное число количество способов добраться конём до правого нижнего угла доски.

def answer(n, m):
    dp = [[0] * m for _ in range(n)]
    dp[0][0] = 1

    for i in range(1, n):
        for j in range(1, m):
            dp[i][j] = (dp[i - 1][j - 2] if j > 1 else 0) + (dp[i - 2][j - 1] if i > 1 else 0)

    return dp[-1][-1]


def test0():
    test_data = ((4, 4), (3, 3), (1, 1))
    for n, m in test_data:
        print(answer(n, m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
