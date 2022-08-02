# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Given a 1-indexed array of integers numbers that is already sorted
# in non-decreasing order, find two numbers such that they add up to
# a specific target number. Let these two numbers be numbers[index1]
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length.
#
# Return the indices of the two numbers, index1 and index2, added by
# one as an integer array [index1, index2] of length 2.
from typing import List


class Solution:
    # my solution
    @staticmethod
    def two_sum(numbers: List[int], target: int) -> List[int]:
        d = {}

        for i, t in enumerate(numbers):

            if t in d:
                return [d[t] + 1, i + 1]
            else:
                d[target - t] = i


if __name__ == '__main__':
    tests = [([2, 7, 11, 15], 9),
             ([2, 3, 4], 6),
             ([-1, 0], -1)]

    for test, test_target in tests:
        print(f'{test} {test_target} -> {Solution.two_sum(test, test_target)}')
