# https://contest.yandex.ru/contest/49329/problems/B/
# Дано два списка чисел, числа в первом списке упорядочены по неубыванию. Для каждого числа из второго списка определите
# номер первого и последнего появления этого числа в первом списке.
#
# Формат ввода.
# В первой строке входных данных записано два числа N и M (1 <= N, M <= 20000). Во второй строке записано N
# упорядоченных по неубыванию целых чисел — элементы первого списка. В третьей строке записаны M целых неотрицательных
# чисел - элементы второго списка. Все числа в списках - целые 32-битные знаковые.
#
# Формат вывода.
# Программа должна вывести M строчек. Для каждого числа из второго списка нужно вывести номер его первого и последнего
# вхождения в первый список. Нумерация начинается с единицы. Если число не входит в первый список, нужно вывести одно
# число 0.

def left_bound(array, key):
    left_index = -1
    right_index = len(array)
    while left_index < right_index - 1:
        mid_index = (left_index + right_index) // 2
        if array[mid_index] < key:
            left_index = mid_index
        else:
            right_index = mid_index

    return left_index


def right_bound(array, key):
    left_index = -1
    right_index = len(array)
    while left_index < right_index - 1:
        mid_index = (left_index + right_index) // 2
        if array[mid_index] <= key:
            left_index = mid_index
        else:
            right_index = mid_index

    return right_index


def lr_search(array, keys):
    for key in keys:
        left, right = left_bound(array, key), right_bound(array, key)
        if right - left > 1:
            print(left + 2, right)
        else:
            print(0)


def lr_search_keyboard_input():
    array = list(map(int, input().split()))
    keys = list(map(int, input().split()))

    for key in keys:
        left, right = left_bound(array, key), right_bound(array, key)
        if right - left > 1:
            print(left + 2, right)
        else:
            print(0)


def test0():
    test_lists = (((1, 3, 5, 5, 5, 7, 7, 7, 7, 100), (1, 3, 5, 6, 7, 8, 9, 100)),
                  ((1, 100, 101, 200, 205), (1, 2, 3)))
    for test_array, test_keys in test_lists:
        lr_search(test_array, test_keys)


def test1():
    for _ in range(2):
        lr_search_keyboard_input()


if __name__ == '__main__':
    tests = (test0, test1)
    for test in tests:
        test()
