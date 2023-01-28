# проверка отсортированности массива за О(N) (однопроходный)
# из лекции Хирьянова https://www.youtube.com/watch?v=2XFaK3bgT7w&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=8

from itertools import product


def check_sorted(array: list, ascending=True):
    sign = 2 * int(ascending) - 1
    for i in range(len(array) - 1):
        if sign * array[i] > sign * array[i + 1]:
            return False

    return True


def test0():
    tests = [[0, 1, 2, 3, 4, 5],
             [0, 2, 1, 3, 4, 4],
             [2, 2, 2, 2, 2, 2],
             [6, 4, 3, 2, 1, 0],
             [4, 4, 4, 4, 4, 1]]

    asc = [True, False]

    for test, asc in product(tests, asc):
        print(check_sorted(test, ascending=asc), sorted(test, reverse=not asc) == test)


if __name__ == '__main__':
    test0()
