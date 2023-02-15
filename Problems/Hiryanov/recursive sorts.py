# пример рекурсивных сортировок
# быстрая сортировка Тони Хоара - hoar sort
# сортировка слияниями Джона фон Неймана - merge sort
# из лекции Хирьянова https://www.youtube.com/watch?v=2XFaK3bgT7w&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=8

def hoar_sort_mem(array: list):
    """
       Быстрая сортировка Тони Хоара - hoar sort mem
       средняя сложность по времени - O(N*log(N))
       худшая сложность по времени - O(N^2)
       сортирующее действие выполняется на прямом ходу рекурсии
       реализация с дополнительной памятью для разделения
       метод - "разделяй и властвуй"
    """
    '''
       обертка для вызова hoar_sort_mem c одним параметром
    '''
    hoar_sort_recursive_auxmem(array, 0, len(array) - 1)


def hoar_sort_lomuto(array: list):
    """
       Сортировка Хоара с методом Ломуто разделения массива (без использования
       дополнительной памяти)
    """
    '''
       обертка для вызова hoar_sort_lomuto c одним параметром
    '''
    hoar_sort_recursive_lomuto(array, 0, len(array) - 1)


def hoar_sort(array: list):
    """
       Быстрая сортировка Тони Хоара - hoar sort
       средняя сложность по времени - O(N*log(N))
       худшая сложность по времени - O(N^2)
       сортирующее действие выполняется на прямом ходу рекурсии
       реализация без дополнительной памяти для разделения (схема Хоара)
       метод - "разделяй и властвуй"
    """
    '''
       обертка для вызова hoar_sort c одним параметром
    '''
    hoar_sort_recursive(array, 0, len(array) - 1)


def partition_hoar(array: list, start: int, finish: int) -> int:
    """
       Алгоритм Хоара разделения данных массива на две части
    """

    pivot = array[start]

    while True:
        while array[start] < pivot:
            start += 1

        while array[finish] > pivot:
            finish -= 1

        if finish <= start:
            return finish

        array[start], array[finish] = array[finish], array[start]
        start += 1
        finish -= 1


def partition_lomuto(array: list, start: int, finish: int) -> int:
    """
       Алгоритм разделения данных массива на две части (разбиение Нико Ломуто) -
       больше опорного элемента (pivot) и меньше либо равных опорному элементу.
       Разделение осуществляется внутри исходного массива - без использования
       вспомогательной памяти. Возвращает индекс опорного элемента.
    """
    pivot = array[finish]
    i = start
    for j in range(start, finish):
        if array[j] <= pivot:
            if i != j:
                array[j], array[i] = array[i], array[j]
            i += 1
    array[i], array[finish] = array[finish], array[i]

    # возвращает индекс опорного элемента - границу двух частей массива
    return i


def partition_auxmem(array: list, start: int, finish: int) -> (int, int):
    # реализация разделения массива на 3 части
    # с выделением дополнительной памяти
    length = finish - start + 1
    pivot = array[start]
    left = 0
    right = length - 1
    tmp = [0] * length
    # сортирующее действие на прямом ходу рекурсии
    for i in range(length):
        if array[start + i] == pivot:
            continue
        if array[start + i] < pivot:
            # print(f'l={left} s={start} i={i}')
            tmp[left] = array[start + i]
            left += 1
        if array[start + i] > pivot:
            # print(f'r={right} s={start} i={i}')
            tmp[right] = array[start + i]
            right -= 1

    for i in range(length):
        if i < left or i > right:
            array[start + i] = tmp[i]
        else:
            array[start + i] = pivot

    return left, right


def hoar_sort_recursive_auxmem(array: list, start: int, finish: int):
    """
        Быстрая сортировка Тони Хоара - hoar sort
        средняя сложность по времени - O(N*log(N))
        худшая сложность по времени - O(N^2)
        сортирующее действие выполняется на прямом ходу рекурсии
        реализация с дополнительной памятью для разделения
        метод - "разделяй и властвуй"
    """
    length = finish - start + 1

    if length < 2:
        return

    left, right = partition_auxmem(array, start, finish)

    hoar_sort_recursive_auxmem(array, start, start + left - 1)
    hoar_sort_recursive_auxmem(array, start + right + 1, finish)


def hoar_sort_recursive_lomuto(array: list, start: int, finish: int):
    """
        Сортировка Хоара с методом Ломуто разделения массива (без использования
        дополнительной памяти)
    """
    length = finish - start + 1

    if length < 2:
        return

    bound = partition_lomuto(array, start, finish)
    # рекурсивно сортируем подмассивы оставляя на месте элемент c индексом bound
    hoar_sort_recursive_lomuto(array, start, bound - 1)
    hoar_sort_recursive_lomuto(array, bound + 1, finish)


def hoar_sort_recursive(array: list, start: int, finish: int):
    """
       Быстрая сортировка Тони Хоара - hoar sort
       средняя сложность по времени - O(N*log(N))
       худшая сложность по времени - O(N^2)
       сортирующее действие выполняется на прямом ходу рекурсии
       реализация без дополнительной памяти для разделения (схема Хоара)
       метод - "разделяй и властвуй"
    """
    length = finish - start + 1

    if length < 2:
        return

    bound = partition_hoar(array, start, finish)

    hoar_sort_recursive(array, start, bound)  # опорный элемент включается!
    hoar_sort_recursive(array, bound + 1, finish)


def merge(a: list, b: list) -> list:
    """
        Функция слияния двух отсортированных списков a и b в третий c
        вызывается как сортировочное действие на обратном ходу рекурсии
        алгоритма фон Неймана (сортировка слияниями)
    """
    c = [0] * (len(a) + len(b))
    k = i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c[k] = a[i]
            i += 1

        else:
            c[k] = b[j]
            j += 1

        k += 1

    while i < len(a):
        c[k] = a[i]
        i += 1
        k += 1

    while j < len(b):
        c[k] = b[j]
        j += 1
        k += 1

    return c


def merge_sort(array: list):
    """
        Сортировка слияниями Джона фон Неймана - merge sort
        сложность по времени (среднее/худшее/лучшее) - O(N*log(N))
        сортирующее действие выполняется на обратном ходу рекурсии
        необходима доп память - О(N)
        метод - "разделяй и властвуй"
    """

    if len(array) < 2:
        return

    middle = len(array) // 2

    # дополнительная память
    left = array[:middle]
    right = array[middle:len(array)]
    merge_sort(left)
    merge_sort(right)
    # сортирующее действие на обратном ходу рекурсии
    array[:] = merge(left, right)[:]


def test(sort_algo):
    print(sort_algo.__doc__)

    tests = [[1, 7, 5, 2, 8, 5, 5],
             [1, 5, 4, 3, 2, 6, 8, 0, 5, 3],
             [1, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4, 4],
             [2, 3, 3, 3, 1, 1, 1, 0, 0, 0, 1, 2, 3, 4],
             [-1, 2, -1, 2, -1, 2, 1, 2, 2, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -100],
             [10, 11, 22, 33, 44, 0, 1, 2, 3, 4, 5],
             [9, 8, 7, 6, 5, 4, 3, 2, 1, 0, -1, -2, -3, -4]]

    for num, test_unsorted in enumerate(tests):
        test_sorted = test_unsorted.copy()
        sort_algo(test_sorted)
        print(f"testcase #{num}: ", "Ok!" if test_sorted == sorted(test_unsorted) else "Failed!")

    print('')


def test0():
    for algo in [hoar_sort, hoar_sort_mem, hoar_sort_lomuto, merge_sort]:
        test(algo)


def test1():
    a = [1, 5, 4, 3, 3, 1, 2, 1, 0, 6, 8, 0, 5, 3]
    print(a)
    hoar_sort(a)
    print(a)


def test2():
    a = [1, 2, 3, 7, 8, 9]
    b = [-1, 0, 1, 2, 10, 11, 12, 13]
    print(merge(a, b))


def test3():
    a = [1, 7, 5, 2, 8, 5, 5]
    print(a)
    partition_lomuto(a, 0, len(a) - 1)
    print(a)


def test4():
    tests = [[2, 1, 7, 5, 0, 1, 2, 0, -1, 8, 5, 5, 2],
             [2, 2, 2, 2, 7, 2, 2, 2, 2, 6, 2, 2, 2, 2],
             [1, 5, 4, 3, 2, 6, 8, 0, 5, 3],
             [1, 7, 5, 2, 8, 5, 5]]

    for test_array in tests:
        print(test_array)
        bound = partition_hoar(test_array, 0, len(test_array) - 1)
        print(test_array)
        print(bound)


if __name__ == '__main__':
    test0()
    # test4()
