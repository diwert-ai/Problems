# https://leetcode.com/problems/search-in-rotated-sorted-array/
# There is an integer array nums sorted in ascending order (with distinct values).
#
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot
# index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ...,
# nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed).
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
#
# You must write an algorithm with O(log n) runtime complexity.

from typing import List


#  my solution
class Solution:
    @staticmethod
    def pivot(array: list):
        """
        search pivot index by binary search - O(log n) runtime complexity
        """
        left = 0
        n = right = len(array)

        while right - left > 1:
            middle = (left + right) // 2
            if array[middle] > array[left]:
                left = middle
            else:
                right = middle

        return n - 1 - left

    @staticmethod
    def left_bound(array: list, p, target):
        """
        search left bound of target by binary search - - O(log n) runtime complexity
        """
        left = -1
        n = right = len(array)

        while right - left > 1:
            middle = (left + right) // 2
            if array[(middle - p) % n] < target:
                left = middle
            else:
                right = middle

        return left

    @staticmethod
    def search(nums: List[int], target: int) -> int:
        p = Solution.pivot(nums)
        index = (Solution.left_bound(nums, p, target) + 1 - p) % len(nums)
        return index if nums[index] == target else -1


def test0():
    tests = [[0, 1, 2, 3, 4, 5, 6, 7]]
    for test_nums in tests:
        print(Solution.search(test_nums, 4))


def test1():
    nums_set = [([4, 5, 6, 1, 2, 3], 1),
                ([1, 2, 3, 4, 5], 3),
                ([5, 1, 2, 3, 4], 2),
                ([1, 2, 3, 4, 0], 0),
                ([3, 4, 5, 1, 2], 7)]
    for nums, target in nums_set:
        print(f'{nums} {target} {Solution.search(nums,target)}')


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
