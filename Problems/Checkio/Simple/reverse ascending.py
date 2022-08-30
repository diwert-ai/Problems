# https://py.checkio.org/en/mission/reverse-every-ascending/
def reverse_ascending(items):
    ret, start_index = [], 0
    for index in range(1, len(items)):
        if items[index] <= items[index-1]:
            ret, start_index = ret+items[start_index:index][::-1], index
    return ret+items[start_index:][::-1]


def test0():
    a = '012345678'
    print(a[0:8])


def test1():
    print("Example:")
    print(reverse_ascending([1, 2, 3, 4, 5]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(reverse_ascending([1, 2, 3, 4, 5])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([5, 7, 10, 4, 2, 7, 8, 1, 3])) == [10, 7, 5, 4, 8, 7, 2, 3, 1]
    assert list(reverse_ascending([5, 4, 3, 2, 1])) == [5, 4, 3, 2, 1]
    assert list(reverse_ascending([])) == []
    assert list(reverse_ascending([1])) == [1]
    assert list(reverse_ascending([1, 1])) == [1, 1]
    assert list(reverse_ascending([1, 1, 2])) == [1, 2, 1]
    print("Coding complete? Click 'Check' to earn cool rewards!")


def test2():
    pass


if __name__ == '__main__':
    tests = [test0, test1, test2]
    for test in tests:
        test()
