# Сортировка подсчетом (для случая, когда множество различных элементов массива конечно (=M)
# и заранее известно)
# сложность О(N) по времени (N - длина массива) и О(M) - по памяти (М - число различных элементов)
# из лекции Хирьянова https://www.youtube.com/watch?v=NLq7nB9bV0M&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=6

def count_sort(array: list, n: list):
    """сортировка подсчетом - count sort"""

    # a - заранее известный список возможных элементов массива

    # словарь частот различные элементов
    f = {m: 0 for m in n}

    # формируем словарь частот за один проход
    for a in array:
        f[a] += 1

    # заполняем array по словарю частот за один проход
    start = 0
    for m in n:
        array[start:start + f[m]] = [m for _ in range(f[m])]
        start += f[m]


def test():
    tests = [([0, 1, 2, 1, 2, 4, 4, 8, 5, 4, 3, 3, 2, 2, 6, 7, 9, 9, 9, 9, 2, 3, 4, 5, 2, 1, 0, 0, 0, 0, 9, 2, 2, 2],
              [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
             ([11, 12, 13, 12, 12, 12, 11, 11, 11, 11, 12], [11, 12, 13]),
             ([1, 11, 1, 1, 1, 1, 1, 1, 1, -1], [-1, 1, 11]),
             ([3, 3, 3, 3, 2, 2, 34, 5, 4, 54, 3, 45, 34, 5, 34, 5, 345, 2], [2, 3, 4, 5, 34, 45, 54, 345])]

    for n, (a_unsorted, m) in enumerate(tests):
        a_sorted = a_unsorted.copy()
        count_sort(a_sorted, m)
        print(f"testcase #{n}: ", "Ok!" if a_sorted == sorted(a_unsorted) else "Failed!")


if __name__ == '__main__':
    test()
