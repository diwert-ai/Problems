def merge(a, b):
    len_a, len_b, a_index, b_index, result_index = len(a), len(b), 0, 0, 0
    result = [0] * (len_a + len_b)

    while a_index < len_a and b_index < len_b:
        if a[a_index] < b[b_index]:
            result[result_index] = a[a_index]
            a_index += 1
        else:
            result[result_index] = b[b_index]
            b_index += 1
        result_index += 1

    if a_index < len_a:
        result[result_index:] = a[a_index:]
    elif b_index < len_b:
        result[result_index:] = b[b_index:]

    return result


def test0():
    arrays = (([1, 2, 3], [3, 4, 5]),
              ([1, 1, 1], [1, 40, 50]),
              ([1, 2, 2, 4], [1, 1, 1, 1]),
              ([], []),
              ([], [1, 2, 4, 7, 9]),
              ([1, 1, 1], []),
              ([1, 2, 3, 4, 4, 4, 4, 4, 5], [4, 4, 6, 6, 7, 7]))
    for a, b in arrays:
        print(merge(a, b))


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
