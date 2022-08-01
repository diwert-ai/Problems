# https://leetcode.com/problems/palindrome-number/
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.


class Solution:
    @staticmethod
    def is_palindrome(x: int) -> bool:
        s = str(x)
        return s == s[::-1]


if __name__ == '__main__':
    tests = [(121, True),
             (3242, False),
             (66, True),
             (8724, False)]

    for test, right_answer in tests:
        print(f'{test} {right_answer} {Solution.is_palindrome(test)}')
