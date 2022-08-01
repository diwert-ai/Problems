# https://leetcode.com/problems/longest-common-prefix/
# Write a function to find the longest common prefix string amongst an array of strings.
# If there is no common prefix, return an empty string "".
from typing import List


class Solution:
    @staticmethod
    def longest_common_prefix(strs: List[str]) -> str:
        l_prefix = ''
        n = len(strs)
        n0 = len(strs[0])

        for j in range(n0):
            c = strs[0][j]
            d = ''
            for i in range(n - 1):
                if j > len(strs[i + 1]) - 1:
                    return l_prefix
                d = d + strs[i + 1][j]

            if (n - 1) * c == d:
                l_prefix = l_prefix + c
            else:
                return l_prefix
        return l_prefix


if __name__ == '__main__':
    tests = [(["flower", "flow", "flight"], "fl"),
             (["dog", "racecar", "car"], "")]

    for test, right_answer in tests:
        print(f'{test} -> "{Solution.longest_common_prefix(test)}" right answer: "{right_answer}"')
