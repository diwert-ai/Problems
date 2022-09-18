﻿from typing import List


class Solution:
    @staticmethod
    def left_bound(array: list, key):
        left = -1
        right = len(array)

        while right - left > 1:
            middle = (left + right) // 2
            if array[middle] < key:
                left = middle
            else:
                right = middle

        return left

    @staticmethod
    def right_bound(array: list, key):
        left = -1
        right = len(array)

        while right - left > 1:
            middle = (left + right) // 2
            if array[middle] <= key:
                left = middle
            else:
                right = middle

        return right

    def search_range(self, nums: List[int], target: int) -> List[int]:
        left = self.left_bound(nums, target)
        right = self.right_bound(nums, target)
        return [left + 1, right - 1] if right - left > 1 else [-1, -1]


def test0():
    nums_tests = [([5, 7, 7, 8, 8, 10], 8),
                  ([5, 7, 7, 8, 8, 10], 6),
                  ([], 0)]
    for nums, target in nums_tests:
        print(Solution().search_range(nums, target))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
