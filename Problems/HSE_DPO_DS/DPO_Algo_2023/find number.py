# В последовательности записаны целые числа. Одно из чисел встречается ровно один раз, остальные - по два раза. Найти
# число, которое встречается один раз.

# В последовательности записаны целые числа. Число X встречается один или два раза, остальные числа - по три раза. Найти
# число X и количество его встреч. Для простоты считаем, что числа неотрицательные и требуют не более 32 бита каждое.

def find_number_double(array):
    result = 0
    for a in array:
        result ^= a

    return result


def find_number_triple(array):
    bin_set = [0] * 32
    result, count, pow2 = 0, 0, 1
    for a in array:
        bin_a = bin(a).split('b')[1]
        j = len(bin_a) - 1
        for i in range(31, 31-len(bin_a), -1):
            bin_set[i] += int(bin_a[j])
            j -= 1

    for i in range(31, -1, -1):
        bin_set[i] %= 3
        if bin_set[i] > 0:
            count = bin_set[i]
            result += pow2
        pow2 *= 2

    return result, count


def test0():
    test_data = ([1, 1, 3, 4, 3, 10, 4, 9, 11, 9, 11],
                 [1, 2, 2, 1, 3, 4, 3],
                 [1, 1, 2, 9, 10, 9, 2])
    for array in test_data:
        print(find_number_double(array))


def test1():
    test_data = ([1, 7, 2, 2, 1, 7, 2, 1, 3, 3, 3],
                 [1, 2, 10, 10, 10, 1, 1])
    for array in test_data:
        print(*find_number_triple(array))


if __name__ == '__main__':
    tests = (test0, test1)
    for test in tests:
        test()
