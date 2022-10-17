# https://leetcode.com/problems/integer-to-roman/
# Given an integer, convert it to a roman numeral.

d1 = {'0': "", '1': "I", '2': "II", '3': "III", '4': "IV", '5': "V", '6': "VI", '7': "VII", '8': "VIII", '9': "IX"}
d2 = {'0': "", '1': "X", '2': "XX", '3': "XXX", '4': "XL", '5': "L", '6': "LX", '7': "LXX", '8': "LXXX", '9': "XC", }
d3 = {'0': "", '1': "C", '2': "CC", '3': "CCC", '4': "CD", '5': "D", '6': "DC", '7': "DCC", '8': "DCCC", '9': "CM", }
d4 = {'0': "", '1': "M", '2': "MM", '3': "MMM"}


class Solution:
    @staticmethod
    def int_to_roman(num: int) -> str:
        lst = list(f'{num:04d}')
        return f'{d4[lst[0]]}{d3[lst[1]]}{d2[lst[2]]}{d1[lst[3]]}'


if __name__ == '__main__':
    tests = [(3, 'III'),
             (58, 'LVIII'),
             (1994, 'MCMXCIV')]

    for test, right_answer in tests:
        print(f'{test} -> {Solution.int_to_roman(test)} right answer: {right_answer}')
