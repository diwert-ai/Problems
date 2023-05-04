# https://contest.yandex.ru/contest/49329/problems/D/
# Дано n отрезков провода длиной l1,l2,…,ln сантиметров. Требуется с помощью разрезания получить из них k равных
# отрезков как можно большей длины, выражающейся целым числом сантиметров. Если нельзя получить k отрезков длиной даже
# 1 см, вывести 0.
#
# Ограничения: 1≤n≤10^4, 1≤k≤10^4, 100≤li≤10^7, все целые числа.

def segments_count(lengths, current_length):
    cnt = 0
    for length in lengths:
        cnt += (length//current_length)
    return cnt


# бинарный поиск по ответу
def max_length_bin_search(segment_lengths, k):
    min_length, max_length = 0, max(segment_lengths)+1

    while min_length < max_length - 1:
        mid_length = (max_length + min_length) // 2
        if segments_count(segment_lengths, mid_length) >= k:
            min_length = mid_length
        else:
            max_length = mid_length

    return min_length


# линейный поиск по ответу
def max_length_enum(segment_lengths, k):
    max_length = max(segment_lengths)
    for length in range(max_length, 0, -1):
        if segments_count(segment_lengths, length) >= k:
            return length
    return 0


def test0():
    test_data = (((802, 743, 457, 539), 11),
                 ((100, 100, 100), 1),
                 ((1000, 1000, 1000), 3))
    for test_list, test_k in test_data:
        print(max_length_bin_search(test_list, test_k))


def test1():
    test_data = (((802, 743, 457, 539), 11),
                 ((100, 100, 100), 1),
                 ((1000, 1000, 1000), 3))
    for test_list, test_k in test_data:
        print(max_length_enum(test_list, test_k))


if __name__ == '__main__':
    tests = (test0, test1)
    for test in tests:
        test()
        print()
