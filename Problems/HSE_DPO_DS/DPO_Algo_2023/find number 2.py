# В последовательности записаны целые числа, больше половины из которых равны одному и тому же числу X. За один просмотр
# последовательности найти это число.

def find_number(array):
    result, count = array[0], 1
    for i in range(1, len(array)):
        if array[i] == result:
            count += 1
        elif count == 1:
            result = array[i]
        else:
            count -= 1

    return result


def test0():
    test_data = ([1, 2, 2, 1, 2, 1, 1, 1, 1, 1, 1],
                 [1, 2, 100, 100, 100, 100],
                 [1, 2, 1, 2, 1],
                 [1, 2, 1, 2, 2],
                 [4, 4, 4, 4, 1, 4, 1, 2, 4, 4, 4, 4, 4, 2, 4, 2, 4, 4, 2, 2, 3, 2, 3, 2, 3],
                 [3, 1, 1, 3, 2, 3, 1, 3, 3],
                 [1, 1, 1, 1, 1, 2, 2, 2, 2])

    for array in test_data:
        print(find_number(array))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
