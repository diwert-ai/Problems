﻿# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Given a string containing digits from 2-9 inclusive,
# return all possible letter combinations that the number could represent.
# Return the answer in any order.
# A mapping of digits to letters (just like on the telephone buttons) is given below.
# Note that 1 does not map to any letters.
from typing import List
from itertools import product


class Solution:
    mapping = {'2': "abc",
               '3': "def",
               '4': "ghi",
               '5': "jkl",
               '6': "mno",
               '7': "pqrs",
               '8': "tuv",
               '9': "wxyz"}

    # мое решение
    @staticmethod
    def letter_combinations(digits: str) -> list[str]:
        res = []
        d = {'2': "abc",
             '3': "def",
             '4': "ghi",
             '5': "jkl",
             '6': "mno",
             '7': "pqrs",
             '8': "tuv",
             '9': "wxyz"}
        n = len(digits)
        if n == 0:
            return res
        for c1 in d[digits[0]]:
            if n == 1:
                res.append(c1)
            else:
                for c2 in d[digits[1]]:
                    if n == 2:
                        res.append(c1+c2)
                    else:
                        for c3 in d[digits[2]]:
                            if n == 3:
                                res.append(c1+c2+c3)
                            else:
                                for c4 in d[digits[3]]:
                                    res.append(c1+c2+c3+c4)
        
        return res

    # второе мое решение
    def letter_combinations2(self, digits: str) -> List[str]:
        if not digits:
            return []
        return list(map(''.join, product(*tuple(map(lambda x: type(self).mapping[x], digits)))))


def test0():
    tests = ['23', '523', '44', '4327']
    for test in tests:
        print(Solution.letter_combinations(test))
        print(Solution().letter_combinations2(test))


if __name__ == '__main__':
    test0()
