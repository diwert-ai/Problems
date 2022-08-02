# https://leetcode.com/problems/3sum-closest/
# Given an integer array nums of length n and an integer target,
# find three integers in nums such that the sum is closest to target.
# Return the sum of the three integers.
# You may assume that each input would have exactly one solution.
from typing import List


class Solution:
    @staticmethod
    def three_sum_t(nums, h, t):
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                s = nums[i] + nums[j]
                if t - s in h and h[t - s] not in (i, j):
                    return True, s + nums[h[t - s]]

        return False, 0

    @staticmethod
    def three_sum_closest(nums: List[int], target: int) -> int:
        nums.sort()
        h = {}
        for i in range(len(nums)):
            h[nums[i]] = i

        k = 0
        while True:
            found, s = Solution.three_sum_t(nums, h, target + k)
            if found:
                return s

            found, s = Solution.three_sum_t(nums, h, target - k)
            if found:
                return s
            k += 1

    # https://leetcode.com/problems/3sum-closest/discuss/7871/Python-O(N2)-solution
    @staticmethod
    def three_sum_closest_mv(num, target):
        num.sort()
        result = num[0] + num[1] + num[2]
        for i in range(len(num) - 2):
            j, k = i + 1, len(num) - 1
            while j < k:
                s = num[i] + num[j] + num[k]
                if s == target:
                    return s

                if abs(s - target) < abs(result - target):
                    result = s

                if s < target:
                    j += 1
                elif s > target:
                    k -= 1

        return result


if __name__ == '__main__':
    tests = [([-13, 592, -501, 770, -952, -675, 322, -829, -246, 657, 608, 485, -112, 967,
              -30, 182, -969, 559, -286, -64, 24, 365, -158, 701, 535, -429, -217, 28, 948, 
              -114, -536, -711, 693, 23, -958, -283, -700, -672, 311, 314, -712, -594, -351, 
              658, 747, 949, 70, 888, 166, 495, 244, -380, -654, 454, -281, -811, -168, -839, 
              -106, 877, -216, 523, -234, -8, 289, -175, 920, -237, -791, -976, -509, -4, -3, 298, 
              -190, 194, -328, 265, 150, 210, 285, -176, -646, -465, -97, -107, 668, 892, 612, -54, 
              -272, -910, 557, -212, -930, -198, 38, -365, -729, -410, 932, 4, -565, -329, -456, 224, 
              443, -529, -428, -294, 191, 229, 112, -867, -163, -979, 236, -227, -388, -209, 984, 188, 
              -549, 970, 951, -119, -146, 801, -554, 564, -769, 334, -819, -356, -724, -219, 527, -405, 
              -27, -759, 722, -774, 758, 394, 146, 517, 870, -208, 742, -782, 336, -364, -558, -417, 
              663, -914, 536, 293, -818, 847, -322, 408, 876, -823, 827, 167], 75460)]

    for test, test_target in tests:
        print(f'{Solution.three_sum_closest_mv(test, test_target)}')
