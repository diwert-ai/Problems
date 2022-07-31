# https://leetcode.com/problems/two-sum/
# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
# You can return the answer in any order.
from typing import List


# my solution
class Solution:
    def two_sum(self, nums: List[int], target: int) -> List[int]:
        i_nums = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in i_nums.keys():
                j = i_nums[diff]
                return [i, j]
            i_nums[nums[i]] = i


if __name__ == '__main__':
    tests = [([2, 7, 11, 15], 9, [0, 1]),
             ([3, 2, 4], 6, [1, 2]),
             ([3, 3], 6, [0, 1])]
    for test_case, (test_nums, test_target, right_answer) in enumerate(tests):
        print(f'test case# {test_case}: {Solution().two_sum(test_nums, test_target)} {right_answer}')
