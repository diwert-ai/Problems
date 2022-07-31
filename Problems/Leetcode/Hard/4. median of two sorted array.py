#https://leetcode.com/problems/median-of-two-sorted-arrays/
#Given two sorted arrays nums1 and nums2 of size m and n respectively, 
#return the median of the two sorted arrays.

class Solution:
    def findMedianSortedArraysBF(self, nums1: list[int], nums2: list[int]) -> float:
        #Brute force Solution O(M+N) операций
        u = (nums1+nums2)
        u.sort()
        l = len(u)
        
        if l%2==1: 
            med = u[(l-1)//2]
        else: 
            med = (u[l//2-1]+u[l//2])/2
        
        return med

    #Fast solution O(Log(min(N,M))) операций
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if(n1>n2):
            nums1,nums2 = nums2,nums1
            n1,n2 = n2,n1
        
        k = (n1+n2-1)//2
        
        l = 0 
        r = min(k,n1)
        
        while(l<r):
            m1 = (l+r)//2
            m2 = k - m1
            
            if nums1[m1]<nums2[m2]:
                l += 1
            else:
                r = m1
        
        a = max(nums1[l-1] if l > 0 else -float('inf'), nums2[k-l] if k-l >= 0 else -float('inf'))
        
        if (n1+n2)%2 == 1:
            return a
        
        b = min(nums1[l] if l < n1 else float('inf'), nums2[k-l+1] if k-l+1 < n2 else float('inf'))
        
        return (a+b)/2

def test0():
    l1 = [1,2,3,4,5,6,7,8,9,10]
    l2 = [3,4,4,6,7,9,100,200,300,301,302]
    sol = Solution()
    print(l1,l2,sol.findMedianSortedArrays(l1,l2), sol.findMedianSortedArraysBF(l1,l2))

if __name__ == '__main__':
    test0()
