# https://leetcode.com/problems/string-to-integer-atoi/
# Implement the myAtoi(string s) function, which converts
# a string to a 32-bit signed integer (similar to C/C++'s atoi function).

# The algorithm for myAtoi(string s) is as follows:

# Read in and ignore any leading whitespace.
# Check if the next character (if not already
# at the end of the string) is '-' or '+'.
# Read this character in if it is either.
# This determines if the final result is negative
# or positive respectively. Assume the result is
# positive if neither is present.
# Read in next the characters until the next non-digit
# character or the end of the input is reached.
# The rest of the string is ignored.
# Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32).
# If no digits were read, then the integer is 0.
# Change the sign as necessary (from step 2).
# If the integer is out of the 32-bit signed integer range [-231, 231 - 1],
# then clamp the integer so that it remains in the range. Specifically,
# integers less than -231 should be clamped to -231, and integers greater
# than 231 - 1 should be clamped to 231 - 1.
# Return the integer as the final result.


class Solution:
    @staticmethod
    def my_atoi(s: str) -> int:
        digits = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}
        n = []
        t = s.strip()
        
        if len(t) == 0:
            return 0
        
        if t[0] == '-':
            sign, i = -1, 1
        elif t[0] == '+':
            sign, i = 1, 1
        else:
            sign, i = 1, 0
            
        while i < len(t):
          
            if t[i] in digits:
                n.append(t[i])
            else:
                break
            
            i += 1
            
        if not n:
            return 0
        else:
            int_n = 0
            pw = 1
            for i in range(len(n)-1, -1, -1):
                int_n += digits[n[i]]*pw
                pw *= 10
                
            res = sign*int_n
            
        if res < -2147483648:
            res = -2147483648
                
        if res > 2147483647:
            res = 2147483647
            
        return res


if __name__ == '__main__':
    tests = [('12342', 12342),
             ('12315644', 12315644),
             ('-67923874', -67923874)]

    for test, right_answer in tests:
        print(f'for test {test} right answer is {right_answer} and solution is {Solution.my_atoi(test)}')
