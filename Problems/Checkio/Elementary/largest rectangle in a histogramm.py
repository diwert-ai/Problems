# https://py.checkio.org/ru/mission/largest-histogram/
# У вас есть гистограмма. Попробуйте найти размер самого
# большого прямоугольника, который можно построить из столбцов гистограммы.
def largest_histogram(histogram):
    result, prev_h_bin, n = 0, -1, len(histogram)
    for i, h_bin in enumerate(histogram):
        if h_bin > prev_h_bin:
            min_bin, result = h_bin, max(result, h_bin)
            for k in range(i+1, n):
                min_bin = min(min_bin, histogram[k])
                result = max(result, min_bin * (k - i + 1))
        prev_h_bin = h_bin

    return result


def test0():
    print(largest_histogram([5]))
    print(largest_histogram([5, 3]))
    print(largest_histogram([1, 1, 4, 1]))
    print(largest_histogram([1, 1, 3, 1]))
    print(largest_histogram([2, 1, 4, 5, 1, 3, 3]))


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("Done! Go check it!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
