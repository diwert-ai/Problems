# Задача. Найти количество пар элементов a и b в отсортированном массиве, такие что b - a > K.

def find_pairs_count(array, k):
    n = len(array)
    count = left = right = 0
    while right < n and array[right] - array[0] <= k:
        right += 1

    while right < n:
        if array[right] - array[left] <= k:
            right += 1
        else:
            count += (n - right)
            left += 1

    return count


def test0():
    test_data = (([1, 3, 7, 10, 15, 30], 10),
                 ([1, 4, 8, 10, 12, 13, 15, 100, 200], 8),
                 )
    for array, k in test_data:
        print(find_pairs_count(array, k))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
