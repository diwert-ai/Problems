# https://www.codewars.com/kata/51b66044bce5799a7f000003
from collections import OrderedDict


# my solution
# noinspection SpellCheckingInspection
class RomanNumerals:
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    d1 = {'0': "", '1': "I", '2': "II", '3': "III", '4': "IV", '5': "V", '6': "VI", '7': "VII", '8': "VIII", '9': "IX"}
    d2 = {'0': "", '1': "X", '2': "XX", '3': "XXX", '4': "XL", '5': "L", '6': "LX", '7': "LXX", '8': "LXXX", '9': "XC"}
    d3 = {'0': "", '1': "C", '2': "CC", '3': "CCC", '4': "CD", '5': "D", '6': "DC", '7': "DCC", '8': "DCCC", '9': "CM"}
    d4 = {'0': "", '1': "M", '2': "MM", '3': "MMM"}

    @classmethod
    def to_roman(cls, val):
        lv = list(f'{val:04d}')
        return f'{cls.d4[lv[0]]}{cls.d3[lv[1]]}{cls.d2[lv[2]]}{cls.d1[lv[3]]}'

    @classmethod
    def from_roman(cls, roman_num):
        result = 0
        list_s = list(roman_num)
        n = len(list_s)
        for i in range(n - 1):
            d_i = cls.roman[list_s[i]]
            if d_i >= cls.roman[list_s[i + 1]]:
                result += d_i
            else:
                result -= d_i
        result += cls.roman[list_s[n - 1]]
        return result


# best practice
# https://www.codewars.com/kata/51b66044bce5799a7f000003/solutions/python?filter=all&sort=best_practice&invalids=false
class RomanNumeralsBP:
    @staticmethod
    def to_roman(num):
        conversions = OrderedDict(
            [('M', 1000), ('CM', 900), ('D', 500), ('CD', 400), ('C', 100), ('XC', 90), ('L', 50), ('XL', 40),
             ('X', 10), ('IX', 9), ('V', 5), ('IV', 4), ('I', 1)])
        out = ''
        for key, value in conversions.items():
            while num >= value:
                out += key
                num -= value
        return out

    @staticmethod
    def from_roman(roman):
        conversions = OrderedDict(
            [('CM', 900), ('CD', 400), ('XC', 90), ('XL', 40), ('IX', 9), ('IV', 4), ('M', 1000), ('D', 500),
             ('C', 100), ('L', 50), ('X', 10), ('V', 5), ('I', 1)])
        out = 0
        for key, value in conversions.items():
            out += value * roman.count(key)
            roman = roman.replace(key, "")
        return out


def test0():
    print(RomanNumerals.from_roman('X'), RomanNumerals.to_roman(3999))


def test1():
    print(RomanNumeralsBP.from_roman('X'), RomanNumeralsBP.to_roman(3999))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
