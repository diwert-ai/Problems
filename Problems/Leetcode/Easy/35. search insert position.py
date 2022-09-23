# https://leetcode.com/problems/search-insert-position/
# Given a sorted array of distinct integers and a target value,
# return the index if the target is found. If not, return the index where
# it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
from typing import List


class Solution:
    @staticmethod
    def search_insert(nums: List[int], target: int) -> int:
        left, right = -1, len(nums)
        while right - left > 1:
            middle = (left + right) // 2
            if nums[middle] < target:
                left = middle
            else:
                right = middle
        return left + 1


def test0():
    nums_tests = [((1, 2, 4, 5, 6, 7, 8), 3, 2),
                  ((4, 5, 6, 7, 8, 9, 10), 9, 5),
                  ((3, 4, 5, 6, 7, 8), 9, 6),
                  ((1, 2, 3, 4, 5, 6, 7, 8), 0, 0)]
    for nums, target, right_answer in nums_tests:
        print(f'result: {Solution.search_insert(nums, target)} answer: {right_answer}')


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
