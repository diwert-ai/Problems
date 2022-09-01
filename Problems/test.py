letters = 'abcdefghijklmnopqrstuvwxyz'


def rot13(message):
    def code(x, alphabet=letters):
        return alphabet[(alphabet.index(x)+13) % 26] if x.isalpha() else x

    return ''.join(code(x) if x.islower() else code(x, letters.upper()) for x in message)


def test0():
    print(rot13('t#est'))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
