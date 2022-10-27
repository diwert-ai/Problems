def _min(*args, **kwargs):
    key, nargs = kwargs.get("key", None), len(args)
    lst = list(args) if nargs > 1 else list(args[0])
    n, min_arg_value = len(lst), None
    if n > 0:
        min_arg_value, min_value = lst[0], key(lst[0]) if key else lst[0]
        for i in range(1, n):
            arg_current, current = lst[i], key(lst[i]) if key else lst[i]
            if current < min_value:
                min_arg_value, min_value = arg_current, current
    return min_arg_value


def _max(*args, **kwargs):
    key, nargs = kwargs.get("key", None), len(args)
    lst = list(args) if nargs > 1 else list(args[0])
    n, max_arg_value = len(lst), None
    if n > 0:
        max_arg_value, max_value = lst[0], key(lst[0]) if key else lst[0]
        for i in range(1, n):
            arg_current, current = lst[i], key(lst[i]) if key else lst[i]
            if current > max_value:
                max_arg_value, max_value = arg_current, current
    return max_arg_value


def test0():
    print(_min('hello'))
    list0 = [(1, 2), (2, 2), (0, 3), (1, 4), (3, -2), (1, 5), (-100, 1)]
    print(_min(list0, key=lambda x: x[1]))
    print(_min(list0, key=lambda x: x[0]))
    print(_min(list0, key=lambda x: -x[1] * 100 - x[0] * 10))


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert _max(3, 2) == 3, "Simple case _max"
    assert _min(3, 2) == 2, "Simple case _min"
    assert _max([1, 2, 0, 3, 4]) == 4, "From a list"
    assert _min("hello") == "e", "From string"
    assert _max(2.2, 5.6, 5.9, key=int) == 5.6, "Two maximal items"
    assert _min([[1, 2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0], "lambda key"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
