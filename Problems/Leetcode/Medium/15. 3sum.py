# https://leetcode.com/problems/3sum/
# Given an integer array nums, return all the triplets
# [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
from typing import List


class Solution:
    # brute force approach O(N^3) time
    @staticmethod
    def three_sum_bf(nums: List[int]) -> List[List[int]]:
        # bf solution
        res = []
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if k != i and nums[i] + nums[j] + nums[k] == 0:
                        tr = sorted([nums[i], nums[j], nums[k]])
                        if tr not in res:
                            res.append(tr)

        return res

    def two_sum(self, a, k):
        res = []
        d = {}
        m = len(a)

        for i in range(m):
            if a[i] in d:
                res.append([i, d[a[i]]])
            else:
                d[k - a[i]] = i

        return res

    def three_sum_2(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []
        for i in range(n):
            r = self.two_sum(nums, -nums[i])
            for dr in r:
                if i not in dr:
                    tr = sorted([nums[i], nums[dr[0]], nums[dr[1]]])
                    if tr not in res:
                        res.append(tr)

        return res

    # my solution O(N^2) time
    @staticmethod
    def three_sum_3(nums: List[int]) -> List[List[int]]:
        res = set()
        d = {}
        f = {}
        new_nums = []
        m = len(nums)

        for i in range(m):
            if nums[i] in f:
                f[nums[i]] += 1
            else:
                f[nums[i]] = 1

            s = f[nums[i]]
            if nums[i] == 0:
                if s < 4:
                    new_nums.append(nums[i])
            else:
                if s < 3:
                    new_nums.append(nums[i])

        nums = new_nums
        m = len(nums)

        for j in range(m):
            for k in range(j + 1, m):
                index = -nums[k] - nums[j]
                if index not in d:
                    d[index] = [(k, j)]
                else:
                    d[index].append((k, j))

        for i in range(m):
            if nums[i] in d:
                for index in d[nums[i]]:
                    if i not in index:
                        j, k = index
                        t = sorted([nums[i], nums[j], nums[k]])
                        res.add(tuple(t))

        return res

    # https://leetcode.com/problems/3sum/discuss/725950/Python-5-Easy-Steps-Beats-97.4-Annotated
    @staticmethod
    def three_sum_l(nums: List[int]) -> List[List[int]]:
        res = set()

        # 1. Split nums into three lists: negative numbers, positive numbers, and zeros
        n, p, z = [], [], []
        for num in nums:
            if num > 0:
                p.append(num)
            elif num < 0:
                n.append(num)
            else:
                z.append(num)

        # 2. Create a separate set for negatives and positives for O(1) look-up times
        N, P = set(n), set(p)

        # 3. If there is at least 1 zero in the list, add all cases where -num exists in N and num exists in P
        #   i.e. (-3, 0, 3) = 0
        if z:
            for num in P:
                if -1 * num in N:
                    res.add((-1 * num, 0, num))

        # 3. If there are at least 3 zeros in the list then also include (0, 0, 0) = 0
        if len(z) >= 3:
            res.add((0, 0, 0))

        # 4. For all pairs of negative numbers (-3, -1), check to see if their complement (4)
        #   exists in the positive number set
        for i in range(len(n)):
            for j in range(i + 1, len(n)):
                target = -1 * (n[i] + n[j])
                if target in P:
                    res.add(tuple(sorted([n[i], n[j], target])))

        # 5. For all pairs of positive numbers (1, 1), check to see if their complement (-2)
        #   exists in the negative number set
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                target = -1 * (p[i] + p[j])
                if target in N:
                    res.add(tuple(sorted([p[i], p[j], target])))

        return res

    # my solution O(N^2) time
    @staticmethod
    def three_sum(nums: List[int]) -> List[List[int]]:
        res = set()
        h = {}
        f = {}
        n = len(nums)
        new_nums = []

        k = 0
        for i in range(n):
            if nums[i] in f:
                f[nums[i]] += 1
            else:
                f[nums[i]] = 1

            s = f[nums[i]]
            if nums[i] == 0:
                if s < 4:
                    new_nums.append(nums[i])
                    h[nums[i]] = k
                    k += 1
            else:
                if s < 3:
                    new_nums.append(nums[i])
                    h[nums[i]] = k
                    k += 1

        nums = new_nums
        n = len(nums)

        for i in range(n):
            for j in range(i + 1, n):
                target = -nums[i] - nums[j]
                if target in h and h[target] not in (i, j):
                    res.add(tuple(sorted([nums[i], nums[j], -nums[i] - nums[j]])))

        return res


if __name__ == '__main__':
    tests = [([-1, 0, 1, 2, -1, -4], [[-1, -1, 2], [-1, 0, 1]]),
             ([0, 1, 1], []),
             ([0, 0, 0], [[0, 0, 0]])]
    for test, right_answer in tests:
        print(f'{test} -> {Solution.three_sum(test)} right answer: {right_answer}')
