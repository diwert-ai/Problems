# https://leetcode.com/problems/4sum/
# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.

class Solution:
    @staticmethod
    def four_sum(nums: list[int], target: int):
        # результирующие множество квадруплетов
        res = set()
        
        # кол-во чисел во входном списке-массиве
        n = len(nums)
        
        # словарь, где будут хранится дополнения к target
        # ключ - величина дополнения, значение - индекс во входном массиве
        h = {}

        # словарь частот. ключ - целое число из входного массива,
        # значение - частота наличия в массиве
        f = {}

        # отфильтрованный массив входных чисел
        new_nums = []
        
        # фильтруем входной массив чисел:
        # после фильтрации 0 должен встречаться не более 3 раз если target
        # отличен от 0
        # другие значения не более 4 раз
        for i in range(n):
            ni = nums[i]
            
            if ni in f:
                f[ni] += 1
            else:
                f[ni] = 1
            
            s = f[ni]
            if ni == 0 and target != 0:
                if s < 4:
                    new_nums.append(ni)
                
            else:
                if s < 5:
                    new_nums.append(ni)
                    
        nums = new_nums
        
        n = len(nums)
            
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    s = nums[i]+nums[j]+nums[k]
                    if s in h and h[s] not in (i, j, k):
                        res.add(tuple(sorted([nums[i], nums[j], nums[k], target-s])))
                    else:
                        h[target-nums[k]] = k
        return res


if __name__ == '__main__':
    test_nums = [1, 0, -1, 0, -2, 2]
    test_target = 0
    print(Solution.four_sum(test_nums, test_target))
