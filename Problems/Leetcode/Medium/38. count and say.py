# https://leetcode.com/problems/count-and-say/
# The count-and-say sequence is a sequence of digit strings defined by the recursive formula:
#
# countAndSay(1) = "1"
# countAndSay(n) is the way you would "say" the digit string from countAndSay(n-1),
# which is then converted into a different digit string.
# To determine how you "say" a digit string, split it into the minimal number of substrings
# such that each substring contains exactly one unique digit. Then for each substring,
# say the number of digits, then say the digit. Finally, concatenate every said digit.
from itertools import groupby


class Solution:
    # my solution
    @staticmethod
    def count_and_say(n: int) -> str:

        def count_and_say_iter(start_list):
            res = []
            current_count, current_number = 0, None

            for item in start_list:
                if item != current_number:
                    res = res + [current_count, current_number] if current_number else res
                    current_count, current_number = 1, item
                else:
                    current_count += 1
            res = res + [current_count, current_number]

            return res

        result = [1]
        for i in range(n - 1):
            result = count_and_say_iter(result)

        return ''.join(map(str, result))

    # clear solution by Stefan Pochmann
    # https://leetcode.com/problems/count-and-say/discuss/15999/4-5-lines-Python-solutions
    @staticmethod
    def count_and_say_clear(n):
        s = '1'
        for _ in range(n - 1):
            s = ''.join(str(len(list(group))) + digit
                        for digit, group in groupby(s))
        return s


def test0():
    print(Solution.count_and_say(15))
    print(Solution.count_and_say_clear(15))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
