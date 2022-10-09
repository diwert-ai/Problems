﻿from typing import List, Tuple
from math import sqrt
from collections import deque


def count_chains(circles: List[Tuple[int, int, int]]) -> int:

    def neighbours(main_circ):
        ret = []
        for circ in circles:
            if main_circ != circ:
                d = sqrt((main_circ[0]-circ[0])**2 + (main_circ[1]-circ[1])**2)
                if (d < circ[2] + main_circ[2] and circ[2] < d + main_circ[2]
                        and main_circ[2] < d + circ[2]):
                    ret.append(circ)
        return ret

    def bfs_circles(start_circle):
        used.add(start_circle)
        queue = deque([start_circle])
        while queue:
            cur_circle = queue.popleft()
            for neighbor in neighbours(cur_circle):
                if neighbor not in used:
                    used.add(neighbor)
                    queue.append(neighbor)

    count, used = 0, set()
    for circle in circles:
        if circle not in used:
            bfs_circles(circle)
            count += 1

    return count


def test0():
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))
    print(count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]))
    print(count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]))
    print(count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
