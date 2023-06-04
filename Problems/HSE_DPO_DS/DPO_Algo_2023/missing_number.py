# Однопроходные алгоритмы.
# В последовательности записаны целые числа от 1 до N в произвольном порядке, но одно из чисел пропущено (остальные
# встречаются ровно по одному разу). N заранее неизвестно. Определить пропущенное.

def get_missing_number(array):
    s, n = 0, 0
    for a in array:
        s += a
        n += 1

    return (n+1)*(n+2) // 2 - s


def test0():
    test_data = ([1, 2, 3, 4],
                 [1, 2, 4, 5],
                 [2, 3, 4, 5],
                 [1, 6, 5, 4, 3],
                 [1, 4, 3, 2])

    for array in test_data:
        print(get_missing_number(array))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
