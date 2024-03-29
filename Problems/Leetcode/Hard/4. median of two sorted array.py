﻿# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.

class Solution:
    @staticmethod
    def find_median_sorted_arrays_bf(nums1: list[int], nums2: list[int]) -> float:
        # Brute force Solution O(M+N) операций
        u = (nums1+nums2)
        u.sort()
        length = len(u)
        
        if length % 2:
            med = u[(length-1)//2]
        else: 
            med = (u[length//2-1]+u[length//2])/2
        
        return med

    # Fast solution O(Log(min(N,M))) операций
    @staticmethod
    def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        if n1 > n2:
            nums1, nums2 = nums2, nums1
            n1, n2 = n2, n1

        k = (n1+n2-1)//2
        
        left = 0
        right = min(k, n1)
        
        while left < right:
            m1 = (left+right)//2
            m2 = k - m1
            
            if nums1[m1] < nums2[m2]:
                left += 1
            else:
                right = m1
        
        a = max(nums1[left-1] if left > 0 else -float('inf'),
                nums2[k-left] if k-left >= 0 else -float('inf'))
        
        if (n1+n2) % 2 == 1:
            return a
        
        b = min(nums1[left] if left < n1 else float('inf'),
                nums2[k-left+1] if k-left+1 < n2 else float('inf'))
        
        return (a+b)/2


def test0():
    l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    l2 = [3, 4, 4, 6, 7, 9, 100, 200, 300, 301, 302]
    print(l1, l2, Solution.find_median_sorted_arrays(l1, l2), Solution.find_median_sorted_arrays_bf(l1, l2))


if __name__ == '__main__':
    test0()
