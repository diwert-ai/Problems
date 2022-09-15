# https://py.checkio.org/en/mission/the-final-stone/
# Your goal is to find the weight of the final stone. If no stones left, the result is 0.
#
# The algorith is very simple:
#
# get the two biggest stones in the batch
# hit and get the resulting stone
# put the resulting stone back in the batch.
# For the Speedy category, you can think about your solution for a million stones
from typing import List
from heapq import heapify, heappop, heappush


# first solution - almost brute force
def final_stone_first(stones: list[int]) -> int:
    if stones:
        stones.sort()
        while len(stones) > 1:
            new_stone, i = stones[-1] - stones[-2], 0
            while i < len(stones) - 2 and stones[i] <= new_stone:
                i += 1
            stones = stones[:i] + [new_stone] + stones[i:-2]
        return stones[0]
    return 0


def left_bound(array: list, key):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] < key:
            left = middle
        else:
            right = middle

    return left


# second solution - using binary search, but slow data structure (list) for insert new element
def final_stone_bin_search(stones: list[int]) -> int:
    if stones:
        stones.sort()
        for _ in range(len(stones) - 1):
            new_stone = stones[-1] - stones[-2]
            left = left_bound(stones[:-2], new_stone) + 1
            stones = stones[:left] + [new_stone] + stones[left:-2]
        return stones[0]
    return 0


# best clear and speedy solution O(n log(n)) time
# https://py.checkio.org/mission/the-final-stone/publications/kurosawa4434/python-3/heapq/?ordering=most_voted&filtering=all
def final_stone_heap(stones: List[int]) -> int:
    heapify(stones_neg := list(map(lambda x: x * -1, stones + [0])))

    for _ in range(len(stones)):
        heappush(stones_neg, heappop(stones_neg) - heappop(stones_neg))

    return heappop(stones_neg) * -1


class Heap:
    def __init__(self):
        self.values = []
        self.size = 0

    # поднять элемент c i го места вверх по дереву так, чтобы
    # структура сохранила свойство кучи
    # вызывается при добавлении нового элемента
    # O(log(size)) - операций
    def sift_up(self, i):
        while i != 0 and self.values[i] > self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    # спустить i-й элемент вниз так, чтобы структура сохранила свойство кучи
    # вызывается после экстракции минимума (максимума) из корня, на место которого
    # перемещается последний элемент, а затем спускается на правильную позицию
    # O(log(size)) - операций
    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i

            if self.values[i] < self.values[2 * i + 1]:
                j = 2 * i + 1

            if 2 * i + 2 < self.size and self.values[j] < self.values[2 * i + 2]:
                j = 2 * i + 2

            if i == j:
                break

            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j

    # добавляем новый элемент в конец
    # затем поднимаем его по дереву (куче) на
    # правильную позицию
    # O(log(size)) - операций
    def insert(self, a):
        self.values.append(a)
        self.size += 1
        self.sift_up(self.size - 1)

    # извлекаем корень (минимальный либо максимальный элемент)
    # кладем на его место последний элемент и спускаем его на
    # правильную позицию в дереве (куче)
    # O(log(size)) - операций
    def extract_max(self):
        # if self.size == 0:
        #     return None

        m = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)

        return m


# трансформация массива в кучу
# O(size*log(size)) - операций
def my_heapify(a: list):
    h = Heap()

    for i in a:
        h.insert(i)

    return h


# быстрая трансформация массива в кучу
# O(size) - операций
def fast_heapify(a: list):
    h = Heap()

    # h.values ссылается на копию 'a' (не на 'a', а именно на копию)
    h.values = a[:]
    h.size = len(a)

    # первую половину элементов (те элементы,
    # которые имеют хотя бы одного потомка) поочередно
    # (в обратном порядке) спускаем по дереву
    # этого достаточно для формирования кучи
    for i in reversed(range(len(a) // 2)):
        h.sift_down(i)

    return h


# third solution - using heap
def final_stone(stones: list[int]) -> int:
    if stones:
        heap = fast_heapify(stones)
        for _ in range(len(stones) - 1):
            heap.insert(heap.extract_max() - heap.extract_max())
        return heap.values[0]
    return 0


def test0():
    from random import randint
    final_stone([3, 5, 1, 1, 9])
    final_stone([1, 2, 3, 4])
    s = [randint(-500000, 500000) for _ in range(1000 * 1000)]
    print(final_stone_heap(s))
    print(final_stone(s))


def test1():
    print('Example:')
    print(final_stone([1, 2, 3]))

    assert final_stone([3, 5, 1, 1, 9]) == 1
    assert final_stone([1, 2, 3]) == 0
    assert final_stone([1, 2, 3, 4]) == 0
    assert final_stone([1, 2, 3, 4, 5]) == 1
    assert final_stone([1, 1, 1, 1]) == 0
    assert final_stone([1, 1, 1]) == 1
    assert final_stone([1, 10, 1]) == 8
    assert final_stone([1, 10, 1, 8]) == 0
    assert final_stone([]) == 0
    assert final_stone([1]) == 1
    assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

    print("The mission is done! Click 'Check Solution' to earn rewards!")


def test3():
    array = [1, 7, 5, 2, 3, 6, 0, 9, 7, 5, 3, 2, 34, 543, 2, 1, 2, 344, 5]
    h = fast_heapify(array)
    while h.values:
        print(h.extract_max(), end=', ')


if __name__ == '__main__':
    test_funcs = [test0, test1, test3]
    for test in test_funcs:
        test()
