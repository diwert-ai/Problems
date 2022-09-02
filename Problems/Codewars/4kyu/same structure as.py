def set_zero(array):
    if type(array) is not list:
        return

    def parse_lst(lst):
        for index, item in enumerate(lst):
            if type(item) is list:
                parse_lst(item)
            else:
                lst[index] = 0
    parse_lst(array)


def same_structure_as(original, other):
    set_zero(l1 := original.copy() if type(original) is list else original)
    set_zero(l2 := other.copy() if type(other) is list else other)
    return l1 == l2


def test0():
    print(same_structure_as([[0], [1]], [[0], [1]]))
    print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
    print(same_structure_as([1, [1, 1]], [1]))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
