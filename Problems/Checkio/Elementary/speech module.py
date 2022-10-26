# https://py.checkio.org/ru/mission/speechmodule/
FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven",
             "eight", "nine"]
SECOND_TEN = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen",
              "sixteen", "seventeen", "eighteen", "nineteen"]
OTHER_TENS = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy",
              "eighty", "ninety"]
HUNDRED = "hundred"


def checkio(number):
    hundreds = number // 100
    tens = (number - hundreds * 100) // 10
    ones = number - 10 * tens - 100 * hundreds
    representation = FIRST_TEN[hundreds - 1] + ' hundred' if hundreds > 0 else ''
    representation = representation + ' ' + OTHER_TENS[tens - 2] if tens > 1 else representation
    representation = representation + ' ' + FIRST_TEN[ones - 1] if tens > 1 and ones > 0 else representation
    representation = representation + ' ' + SECOND_TEN[ones] if tens == 1 else representation
    representation = representation + ' ' + FIRST_TEN[ones - 1] if tens == 0 and ones > 0 else representation

    return representation.lstrip()


def test0():
    for num in (123, 122, 30, 32, 1, 4, 2, 10, 154, 999, 223, 210, 200, 712, 12, 204, 313, 11, 611, 619, 750, 759):
        print(f'{num}: {checkio(num)}')


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio(4) == 'four', "1st example"
    assert checkio(133) == 'one hundred thirty three', "2nd example"
    assert checkio(12) == 'twelve', "3rd example"
    assert checkio(101) == 'one hundred one', "4th example"
    assert checkio(212) == 'two hundred twelve', "5th example"
    assert checkio(40) == 'forty', "6th example"
    assert not checkio(212).endswith(' '), "Don't forget strip whitespaces at the end of string"
    print('Done! Go and Check it!')


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
