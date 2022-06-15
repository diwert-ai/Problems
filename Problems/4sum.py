#https://leetcode.com/problems/4sum/
#Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
#0 <= a, b, c, d < n
#a, b, c, and d are distinct.
#nums[a] + nums[b] + nums[c] + nums[d] == target
#You may return the answer in any order.
class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        res = set()
        
        n=len(nums)
        
        h={}
        f={}
        new_nums =[]
         
        for i in range(n):
            ni = nums[i]
            
            if  ni in f:
                f[ni]+=1
            else:
                f[ni]=1
            
            s = f[ni]
            if ni == 0 and target != 0:
                if s<4:
                    new_nums.append(ni)
                
            else:
                if s<5:
                    new_nums.append(ni)
                    
        nums = new_nums
        
        n = len(nums)
        nums.sort()


            
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    s=nums[i]+nums[j]+nums[k]
                    if s in h and h[s] not in (i,j,k):
                        res.add(tuple(sorted([nums[i],nums[j],nums[k],target-s])))
                    else:
                        h[target-nums[k]]=k
        return res

nums = [1,0,-1,0,-2,2]
target = 0
sol = Solution()

print(sol.fourSum(nums,target))
