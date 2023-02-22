# словарь для расшифровки римских цифр
roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}


def roman_to_int(s):
    result = 0
    list_s = list(s)
    n = len(list_s)
    for i in range(n - 1):
        d_i = roman[list_s[i]]
        if d_i >= roman[list_s[i + 1]]:
            result += d_i
        else:
            result -= d_i
    result += roman[list_s[n - 1]]
    return result


def test0():
    tests = ('V', 'XXIV', 'LXXXIX', 'XLIV', 'XCIX', 'MDCCCXXVII', 'MCMLXXXII', 'MMXXIII', 'MMMMMV', 'DCLXVI',
             'MMMMMMMMMCMXCIX')
    for roman_num in tests:
        print(f'{roman_num} -> {roman_to_int(roman_num)}')


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
