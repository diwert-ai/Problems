# https://leetcode.com/problems/integer-to-roman/
# Given an integer, convert it to a roman numeral.

first = {
    '0': "",
    '1': "I",
    '2': "II",
    '3': "III",
    '4': "IV",
    '5': "V",
    '6': "VI",
    '7': "VII",
    '8': "VIII",
    '9': "IX"}

second = {
    '0': "",
    '1': "X",
    '2': "XX",
    '3': "XXX",
    '4': "XL",
    '5': "L",
    '6': "LX",
    '7': "LXX",
    '8': "LXXX",
    '9': "XC",
}

third = {
    '0': "",
    '1': "C",
    '2': "CC",
    '3': "CCC",
    '4': "CD",
    '5': "D",
    '6': "DC",
    '7': "DCC",
    '8': "DCCC",
    '9': "CM",
}

forth = {
    '0': "",
    '1': "M",
    '2': "MM",
    '3': "MMM",
}


class Solution:
    @staticmethod
    def int_to_roman(num: int) -> str:
        lst = list(f'{num:04d}')
        return f'{forth[lst[0]]}{third[lst[1]]}{second[lst[2]]}{first[lst[3]]}'


if __name__ == '__main__':
    tests = [(3, 'III'),
             (58, 'LVIII'),
             (1994, 'MCMXCIV')]

    for test, right_answer in tests:
        print(f'{test} -> {Solution.int_to_roman(test)} right answer: {right_answer}')
