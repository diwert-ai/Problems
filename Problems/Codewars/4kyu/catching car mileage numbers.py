# https://www.codewars.com/kata/52c4dd683bfd3b434c000292

def is_interesting(number, awesome_phrases):

    def interesting(n):
        if n in awesome_phrases:
            return True
        if (m := len(sn := str(n))) > 2:
            if sn == sn[::-1]:  # the digits are a palindrome
                return True
            if len(set(sn)) == 1:  # every digit is the same number
                return True
            if list(sn[1:]) == ['0']*(m-1):  # any digit followed by all zeros
                return True
            if sn.find('0') in (-1, m-1):
                sequence = list(map(int, sn))
                if sequence == [(int(sn[0])+i) % 10 for i in range(m)]:   # The digits are sequential +
                    return True
                if sequence == [(int(sn[0])-i) % 10 for i in range(m)]:   # The digits are sequential -
                    return True
        return False

    return 2 if interesting(number) else (1 if interesting(number + 1) or interesting(number + 2) else 0)


def test0():
    tests = [
        {'n': 3, 'interesting': [1337, 256], 'expected': 0},
        {'n': 1336, 'interesting': [1337, 256], 'expected': 1},
        {'n': 1337, 'interesting': [1337, 256], 'expected': 2},
        {'n': 11208, 'interesting': [1337, 256], 'expected': 0},
        {'n': 11209, 'interesting': [1337, 256], 'expected': 1},
        {'n': 11211, 'interesting': [1337, 256], 'expected': 2},
        {'n': 800, 'interesting': [1337, 256], 'expected': 2},
        {'n': 110, 'interesting': [1337, 256], 'expected': 1}
    ]
    for test_item in tests:
        print(f'{is_interesting(test_item["n"], test_item["interesting"])} : {test_item["expected"]}')


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
