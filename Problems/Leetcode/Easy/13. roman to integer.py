# https://leetcode.com/problems/roman-to-integer/


class Solution:
    @staticmethod
    def roman_to_int(s: str) -> int:
        result = 0
        roman = {'I': 1,
                 'V': 5,
                 'X': 10,
                 'L': 50,
                 'C': 100,
                 'D': 500,
                 'M': 1000}
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


if __name__ == '__main__':
    tests = [("III", 3),
             ("LVIII", 58),
             ("MCMXCIV", 1994)]
    for test_case, (test_s, right_answer) in enumerate(tests):
        print(f'test case#{test_case}: {Solution.roman_to_int(test_s)} == {right_answer}')
