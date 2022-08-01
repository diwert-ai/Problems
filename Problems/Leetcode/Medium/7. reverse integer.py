# https://leetcode.com/problems/reverse-integer/
# Given a signed 32-bit integer x, return x with
# its digits reversed. If reversing x causes the
# value to go outside the signed 32-bit integer
# range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to
# store 64-bit integers (signed or unsigned).


class Solution:
    @staticmethod
    def reverse(x: int) -> int:
        sign = -1 if x < 0 else 1
        s = str(x * sign)
        y = s[::-1]
        z = int(y)
        if z > 2 ** 31 - 1:
            z = 0
        return z * sign


if __name__ == '__main__':
    tests = (1231223, -12134, 12312, 534159, -1231345)
    for test in tests:
        print(f'{test}<->{Solution.reverse(test)}')
