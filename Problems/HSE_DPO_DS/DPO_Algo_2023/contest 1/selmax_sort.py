# https://contest.yandex.ru/contest/49089/problems/C/
# Требуется отсортировать массив по неубыванию методом "выбор максимума".
# Зачтенная посылка https://contest.yandex.ru/contest/49089/run-report/86291202/
import random


def select_max_sort(array):
    n = len(array)
    for i in range(n - 1, -1, -1):
        max_index = i
        for j in range(i - 1, -1, -1):
            if array[j] > array[max_index]:
                max_index = j
        array[i], array[max_index] = array[max_index], array[i]
    return array


def test():
    tests = ([1, 3, 4, 1, 3, -1, 2, -1, 2, 3],
             [3, 4, 5, 3, 4, 2],
             [random.randint(-1000, 1000) for _ in range(random.randint(1, 10))],
             [random.randint(-1000, 1000) for _ in range(random.randint(1, 10))],
             )
    for test_array in tests:
        print(*test_array)
        print(*select_max_sort(test_array))
        print()


if __name__ == '__main__':
    test()
