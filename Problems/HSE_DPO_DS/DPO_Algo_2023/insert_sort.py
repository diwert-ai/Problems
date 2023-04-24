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
    pass


if __name__ == '__main__':
    test()

