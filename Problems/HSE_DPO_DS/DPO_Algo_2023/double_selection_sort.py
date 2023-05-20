# двухсторонняя сортировка выбором
# https://habr.com/ru/articles/422085/


def double_selection_sort(array):
    n = len(array)
    for i in range(0, n // 2 + 1):
        min_element = i
        max_element = n - 1 - i

        for j in range(i, n - i):
            if array[j] < array[min_element]:
                min_element = j
            if array[j] > array[max_element]:
                max_element = j

        if max_element == i and min_element == n - 1 - i:
            array[max_element], array[min_element] = array[min_element], array[max_element]
        elif max_element == i:
            array[max_element], array[n - 1 - i] = array[n - 1 - i], array[max_element]
            array[min_element], array[i] = array[i], array[min_element]
        elif min_element != i or max_element != (n - 1 - i):
            array[min_element], array[i] = array[i], array[min_element]
            array[max_element], array[n - 1 - i] = array[n - 1 - i], array[max_element]


def test0():
    arrays = ([0, 8, 7, 2],
              [9, 3, 0, 8, 4],
              [8, 9, 7, 5, 0],
              [9, 3, 4, 7, -1],
              [3, 1, 8, -4]
              )
    for a in arrays:
        double_selection_sort(a)
        print(*a)


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
