def adjacent_letters(line: str) -> str:
    while True:
        exclude_list, k = [], 0
        while k < len(line) - 1:
            if line[k] == line[k+1]:
                exclude_list.append(k)
                exclude_list.append(k+1)
                k += 2
            else:
                k += 1
        if exclude_list:
            line = ''.join(line[i] for i in range(len(line)) if i not in exclude_list)
        else:
            return line


def test0():
    print(adjacent_letters('aaa'))
    print(adjacent_letters("lllllet's get rrready to the rrrummmmmble!"))


def test1():
    print("Example:")
    print(adjacent_letters("abbaca"))

    assert adjacent_letters("adjacent_letters") == "adjacent_lrs"
    assert adjacent_letters("") == ""
    assert adjacent_letters("aaa") == "a"
    assert adjacent_letters("ABBA") == ""

    print("The mission is done! Click 'Check Solution' to earn rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
