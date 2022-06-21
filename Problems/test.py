from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        i = 1
        j = 0
        while j < len(nums) and i < len(nums):
            while  nums[j] == nums[i-1]: 
                j += 1
                if j == len(nums):
                    break
            
            if j == len(nums):
                break

            nums[i]=nums[j]
            i+=1

                      
                
        for j in range(i,len(nums)):
            nums[j] = '_'
            
        return i


if __name__ == '__main__':
    nums = [1,2,3,4]
    print(Solution().removeDuplicates(nums))
    print(nums)


