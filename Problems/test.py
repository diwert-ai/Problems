from typing import List


# noinspection SpellCheckingInspection
class BColors:
    WARNING = '\033[93m'
    ENDC = '\033[0m'


class Solution:
    @staticmethod
    def next_permutation(nums: List[int]) -> None:
        n = len(nums)
        s = n - 1
        while s >= 1 and nums[s] <= nums[s - 1]:
            s -= 1
        if s:
            suffix, next_suffix, j = nums[s - 1], nums[s], s
            for i in range(s, n):
                if next_suffix >= nums[i] > suffix:
                    next_suffix, j = nums[i], i
            nums[j], nums[s - 1] = suffix, next_suffix
            for i in range(s, (s + n) // 2):
                nums[i], nums[n - 1 - i + s] = nums[n - 1 - i + s], nums[i]
        else:
            nums.reverse()


def test0():
    tests = (([1, 2, 5, 3, 4], [1, 2, 5, 4, 3]),
             ([1, 2, 3, 4], [1, 2, 4, 3]),
             ([7, 6, 3, 5, 2, 4, 1], [7, 6, 3, 5, 4, 1, 2]),
             ([7, 4, 3, 2, 6, 5, 1], [7, 4, 3, 5, 1, 2, 6]),
             ([1, 2, 3], [1, 3, 2]),
             ([1, 5, 5, 3, 2, 5, 5], [1, 5, 5, 3, 5, 2, 5]))
    for (perm, next_perm) in tests:
        copy_perm = perm.copy()
        Solution.next_permutation(perm)
        print(f'{copy_perm} -> {perm} : {next_perm} {BColors.WARNING}{perm==next_perm}{BColors.ENDC}')


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
