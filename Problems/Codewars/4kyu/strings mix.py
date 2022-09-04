# https://www.codewars.com/kata/5629db57620258aa9d000014
def mix(s1, s2):
    # noinspection SpellCheckingInspection
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = []
    for letter in letters:
        c1, c2 = s1.count(letter), s2.count(letter)
        if max(c1, c2) < 2:
            continue
        if c1 > c2:
            result.append('1:' + letter*c1)
        elif c1 == c2:
            result.append('=:' + letter*c1)
        else:
            result.append('2:' + letter*c2)

    return '/'.join(sorted(result, key=lambda x: (-len(x), x)))


def test0():
    print(mix("Are they here", "yes, they are here"))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
