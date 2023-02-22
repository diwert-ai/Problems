# вычисляет декартово произведение аргументов
def product(*args):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


mapping = {'2': "abc",
           '3': "def",
           '4': "ghi",
           '5': "jkl",
           '6': "mno",
           '7': "pqrs",
           '8': "tuv",
           '9': "wxyz"}


def letter_combinations(digits):
    if not digits:
        return []
    return list(map(''.join, product(*tuple(map(lambda x: mapping[x], digits)))))


def test0():
    tests = ('23', '523', '44', '4327')
    for digits in tests:
        print(letter_combinations(digits))


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
