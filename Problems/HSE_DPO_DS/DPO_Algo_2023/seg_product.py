# Задача. Эффективно вычислять произведение на отрезке массива от i до j.
from num_zeroes import num_zeroes


def seg_product(array, queries):
    n = len(array)
    num_z = num_zeroes(array, queries)
    results = [0] * len(queries)
    products = [1] * (n + 1)
    for i in range(1, n+1):
        a_i = array[i-1]
        products[i] = (products[i-1] * a_i if a_i else 1)

    for k, (i, j) in enumerate(queries):
        results[k] = (0 if num_z[k] else products[j+1]/products[i])

    return results


def test0():
    test_data = (([2, 2, 3, 4, 5, 0, 4, 5, 6, 7], ((0, 2), (0, 6), (3, 5), (2, 4), (6, 8), (0, 9))), )
    for array, queries in test_data:
        print(*seg_product(array, queries))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
