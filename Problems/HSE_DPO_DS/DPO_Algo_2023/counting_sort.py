# сортировка подсчетом


def counting_sort(array):
    shift = min(array)
    k = max(array) - shift + 1
    n, index, c = len(array), 0, [0] * k
    for i in range(n):
        c[array[i] - shift] += 1
    for i in range(k):
        for j in range(c[i]):
            array[index] = i + shift
            index += 1


def counting_sort_stabled(array):
    shift = min(array)
    k = max(array) - shift + 1
    n, c = len(array), [0] * k
    result = [0] * n
    for i in range(n):
        c[array[i] - shift] += 1
    for i in range(1, k):
        c[i] += c[i - 1]
    for i in range(n - 1, -1, -1):
        a_i = array[i]
        c[a_i - shift] -= 1
        result[c[a_i - shift]] = a_i
    return result


def test0():
    arrays = ([-2, 1, 0, -7, 2, 3, 10, 7, 7, -2, 4, 3, 3, -7, -7, -7, 3, 0],
              [-3, -7, -7, -1, -2, -3, -3, -3])
    print('non stabled sort')
    for a in arrays:
        print(*sorted(a))
        print(*a)
        counting_sort(a)
        print(*a)
    print('---------')


def test1():
    arrays = ([-2, 1, 0, -7, 2, 3, 10, 7, 7, -2, 4, 3, 3, -7, -7, -7, 3, 0],
              [-3, -7, -7, -1, -2, -3, -3, -3])
    print('stabled sort')
    for a in arrays:
        print(*sorted(a))
        print(*a)
        print(*counting_sort_stabled(a))
    print('---------')


if __name__ == '__main__':
    tests = (test0, test1)
    for test in tests:
        test()
