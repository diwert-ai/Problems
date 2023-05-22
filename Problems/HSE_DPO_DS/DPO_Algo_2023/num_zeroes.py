# Задача. Эффективно вычислять число нулей на отрезке от i до j.

def num_zeroes(array, queries):
    n = len(array)
    zeros_count = [0] * n
    count = 0
    result = [0] * len(queries)
    for i in range(n):
        if not array[i]:
            count += 1
        zeros_count[i] = count

    for k, (i, j) in enumerate(queries):
        result[k] = zeros_count[j] - zeros_count[i] + (1 if not array[i] else 0)

    return result


def test0():
    test_data = (([0, 1, 2, 0, 2, 0, 2, 2, 4, 5, 6, 0, 0], ((0, 0), (1, 4), (1, 8), (4, 11), (1, 11))), )

    for array, queries in test_data:
        print(*num_zeroes(array, queries))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
