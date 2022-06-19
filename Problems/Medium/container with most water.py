#https://leetcode.com/problems/container-with-most-water/submissions/
#You are given an integer array height of length n. 
#There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
#Find two lines that together with the x-axis form a container, such that the container contains the most water.
#Return the maximum amount of water a container can store.
#Notice that you may not slant the container.

class Solution:
    def maxAreaBF(self, height: list[int]) -> int:
        #brute force solution O(N**2) операций
        s = 0
        l = len(height)
        
        for i in range(l):
            for j in range(i+1,l):
                s_cur = min(height[i],height[j])*(j-i)
                if s_cur>s: s=s_cur                       
        return s

    #fast solution O(N) операций O(1) - память
    #метод двух указателей
    def maxArea(self, height: list[int]) -> int:       
        s = 0
        left = 0
        right = len(height)-1
                
        while(left<right):   
            h_l = height[left]
            h_r = height[right]
                       
            if h_l > h_r:
                s = max(s,h_r*(right-left))
                right-=1                              
            else:
                s = max(s,h_l*(right-left))
                left+=1        
        return s

def test0():
    height = [1,8,6,2,5,4,8,3,7,4,5,3,2,1,2,2,3,2,32,1,23]
    sol = Solution()

    print(sol.maxArea(height), sol.maxAreaBF(height))

if __name__ == '__main__':
    test0()