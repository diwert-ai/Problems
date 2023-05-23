# Задача. Дан массив и скользящее окно длины k. Эффективно найти минимум в каждом окне массива.
from collections import deque


def window_minimums(array, k):
    n, queue, result = len(array), deque([array[0]]), list()

    for i in range(1, n):
        a_i = array[i]
        while queue and a_i < queue[0]:
            queue.popleft()
        queue.appendleft(a_i)
        if i >= k - 1:
            result.append(queue[-1])
            if array[i - (k - 1)] == queue[-1]:
                queue.pop()

    return result


def test0():
    test_data = (
                    ([4, 2, 6, 7, 6, 8], 3),
                    ([2, 0, 1, 4, 7, 8, 1, 3, 2, 4, 5, 7, 3, 8, 5, 6, 2], 4)
                )
    for array, k in test_data:
        print(*window_minimums(array, k))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
