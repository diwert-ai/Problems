def greatest_common_divisor(*args: int) -> int:
    def gcd_p(a, b):
        return a if b == 0 else gcd_p(b, a % b)
    d = args[0]
    for i in range(1, len(args)):
        d = gcd_p(d, args[i])
    return d


def test0():
    print(greatest_common_divisor(1, 2, 3, 4))
    pass


def test1():
    print("Example:")
    print(greatest_common_divisor(6, 4))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert greatest_common_divisor(6, 4) == 2
    assert greatest_common_divisor(2, 4, 8) == 2
    assert greatest_common_divisor(2, 3, 5, 7, 11) == 1
    assert greatest_common_divisor(3, 9, 3, 9) == 3
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
