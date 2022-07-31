# https://leetcode.com/problems/divide-two-integers/

# Given two integers dividend and divisor, divide two integers
# without using multiplication, division, and mod operator.
# The integer division should truncate toward zero, which means
# losing its fractional part. For example, 8.345 would be truncated
# to 8, and -2.7335 would be truncated to -2.
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store
# integers within the 32-bit signed integer range: [−2**31, 2**31 − 1].
# For this problem, if the quotient is strictly greater than 2**31 - 1,
# then return 2**31 - 1, and if the quotient is strictly less than -2**31,
# then return -231.

class Solution:
    # my solution
    @staticmethod
    def divide(dividend: int, divisor: int) -> int:
        sign = -1 if (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0) else 1
        a_divisor = abs(divisor)
        a_dividend = abs(dividend)
        if a_divisor > a_dividend:
            return 0
        elif divisor == dividend:
            return 1
        elif divisor + dividend == 0:
            return -1
        elif divisor == 1:
            return min(dividend, 2 ** 31 - 1) if dividend > 0 else max(dividend, -2 ** 31)
        elif divisor == -1:
            return min(-dividend, 2 ** 31 - 1) if dividend < 0 else max(-dividend, -2 ** 31)

        t_dividend = a_dividend
        quotient = 0
        while t_dividend >= a_divisor:
            pow2a, pow2 = a_divisor, 1
            while t_dividend - pow2a - pow2a >= 0:
                pow2a += pow2a
                pow2 += pow2
            if sign == 1:
                quotient += pow2
            else:
                quotient -= pow2
            t_dividend -= pow2a

        return quotient

    # most voted https://leetcode.com/problems/divide-two-integers/discuss/142849/C%2B%2BJavaPython-Should-Not-Use-%22long%22-Int
    def divide_mv(self, A, B):
        if (A == -2147483648 and B == -1): return 2147483647
        a, b, res = abs(A), abs(B), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += 1 << x
                a -= b << x
        return res if (A > 0) == (B > 0) else -res

    # clear version https://leetcode.com/problems/divide-two-integers/discuss/13403/Clear-python-code
    def divide_clear(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)


if __name__ == '__main__':
    a = 17*(2**3+2**5)
    b = -3
    print(f'a={a} b={b}\ntrue result: {int(a/b)}\nmy result: {Solution().divide(a, b)}')


