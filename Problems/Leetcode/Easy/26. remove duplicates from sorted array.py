# https://leetcode.com/problems/remove-duplicates-from-sorted-array/

# Given an integer array nums sorted in non-decreasing order,  
# remove the duplicates in-place such that each unique element appears only once.
# The relative order of the elements should be kept the same.
# Since it is impossible to change the length of the array in some languages,  
# you must instead have the result be placed in the first part of the array nums. 
# More formally,  if there are k elements after removing the duplicates,  
# then the first k elements of nums should hold the final result. 
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array.
# You must do this by modifying the input array in-place with O(1) extra memory.
from typing import List


class Solution:
    # мое решение O(n) - время; O(1)  - память
    @staticmethod
    def remove_duplicates(nums: List[int]) -> int:
        i = 1
        j = 0
        while j < len(nums) and i < len(nums):
            while nums[j] == nums[i-1]: 
                j += 1
                if j == len(nums):
                    break
            
            if j == len(nums):
                break

            nums[i] = nums[j]
            i += 1
                      
        for _ in range(i, len(nums)):
            nums.pop()
            
        return i

    # решение most voted
    # https://leetcode.com/problems/remove-duplicates-from-sorted-array/discuss/302016/Python-Solution
    @staticmethod
    def remove_duplicates_mv(nums: List[int]) -> int:        
        x = 1
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                nums[x] = nums[i+1]
                x += 1
        return x


def test0():
    m = [1, 2, 2, 2, 2, 3, 3, 3, 4, 7, 7, 7, 8, 9, 9, 9, 9, 20]

    print(Solution.remove_duplicates(m))
    print(m)


if __name__ == '__main__':
    test0()
