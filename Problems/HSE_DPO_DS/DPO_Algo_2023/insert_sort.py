# https://contest.yandex.ru/contest/49089/problems/B/
# Вам необходимо реализовать сортировку простыми вставками по неубыванию и посчитать количество элементов,
# которые при добавлении к сортированной части уже находились на своём месте, то есть которые не пришлось двигать.
# зачтенная посылка: https://contest.yandex.ru/contest/49089/run-report/86353894/

def insert_sort(array):
    cnt, n = 0, len(array)
    for i in range(1, n):
        key, j = array[i], i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j -= 1

        if i == j + 1:
            cnt += 1
        array[j + 1] = key

    return array, cnt


def test():
    tests = (([1, 2, 5, 3, 4], 2),
             ([1, 2, 3, 4, 5], 4),
             ([2, 2, 2, 2, 2], 4),
             ([5, 4, 3, 2, 1], 0)
             )
    for test_array, right_answer in tests:
        print(*test_array)
        sorted_array, answer = insert_sort(test_array)
        print(*sorted_array)
        print(f'right answer: {right_answer}')
        print(f'answer: {answer}')
        print()


if __name__ == '__main__':
    test()
