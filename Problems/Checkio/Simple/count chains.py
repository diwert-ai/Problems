# https://py.checkio.org/en/mission/count-chains/
# In this mission you must count chains.
#
# You are given a list of details of the circle (tuple of X-coordinate, Y-coordinate, radius).
# You have to return the number of groups of circles where their circumferences intersect.
#
# NOTE:
#
# Only one circle counts as one group.
from typing import List, Tuple
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
    print("Example:")
    print(count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert count_chains([(1, 1, 1), (4, 2, 1), (4, 3, 1)]) == 2, 'basic'
    assert count_chains([(1, 1, 1), (2, 2, 1), (3, 3, 1)]) == 1, 'basic #2'
    assert count_chains([(2, 2, 2), (4, 2, 2), (3, 4, 2)]) == 1, 'trinity'
    assert count_chains([(2, 2, 1), (2, 2, 2)]) == 2, 'inclusion'
    assert count_chains([(1, 1, 1), (1, 3, 1), (3, 1, 1), (3, 3, 1)]) == 4, 'adjacent'
    assert count_chains([(0, 0, 1), (-1, 1, 1), (1, -1, 1), (-2, -2, 1)]) == 2, 'negative coordinates'
    assert count_chains([(1, 3, 1), (2, 2, 1), (4, 2, 1), (5, 3, 1), (3, 3, 1)]) == 1
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
