# https://contest.yandex.ru/contest/49613/problems/D/
# У Олега есть матрица целых чисел n×m. Его очень часто просят узнать сумму всех элементов матрицы в прямоугольнике с
# левым верхним углом (x1, y1) и правым нижним (x2, y2). Помогите ему в этом.

def matrix_sums(matrix, queries):
    n, m, results = len(matrix), len(matrix[0]), list()
    sums = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            sums[i][j] = sums[i - 1][j] + sums[i][j - 1] - sums[i - 1][j - 1] + matrix[i - 1][j - 1]

    for x1, y1, x2, y2 in queries:
        results.append(sums[x2][y2] - sums[x2][y1 - 1] - sums[x1 - 1][y2] + sums[x1 - 1][y1 - 1])

    return results


def test0():
    test_data = (([[1, 2, 3, 4, 5, 6],
                   [7, 8, 9, 10, 11, 12],
                   [13, 14, 15, 16, 17, 18]],
                  ((1, 2, 2, 6), (1, 4, 1, 5), (1, 4, 2, 4),
                   (2, 3, 2, 6), (1, 3, 2, 5), (3, 1, 3, 1))),
                 )

    for matrix, queries in test_data:
        print(matrix_sums(matrix, queries))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
