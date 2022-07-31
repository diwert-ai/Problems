# https://leetcode.com/problems/remove-element/solution/
# Given an integer array nums and an integer val, remove all
# occurrences of val in nums in-place. The relative order of the elements may be changed.


from typing import List


# my solution
class Solution:
    @staticmethod
    def remove_element(nums: List[int], val: int) -> int:
        n = len(nums)
        k = 0
        left = 0
        right = n - 1
        print(f'l={left} r={right} k={k} {nums}')
        while left <= right:
            while nums[right] == val and right > -1:
                right -= 1
                k += 1
            if nums[left] == val and left < right:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
                k += 1

            left += 1
            print(f'l={left} r={right} k={k} {nums}')

        return n - k

    # most voted https://leetcode.com/problems/remove-element/discuss/12584/6-line-Python-solution-48-ms
    def remove_element_mv(self, nums, val):
        i = 0
        for x in nums:
            if x != val:
                nums[i] = x
                i += 1
        return i


if __name__ == '__main__':
    tests = [[0, 1, 0, 1, 0],
             [1],
             [1, 1],
             [1, 0, 1],
             [0, 1, 0],
             [1, 1, 0]]
    for test in tests:
        print(test, Solution.remove_element(test, 1))
