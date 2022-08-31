# https://py.checkio.org/ru/mission/bigger-together/

from typing import List
from functools import cmp_to_key


def bigger_together(ints: List[int]) -> int:
    ordered = sorted(map(str, ints), key=cmp_to_key(lambda x, y: int(x+y) - int(y+x)))
    return int(''.join(ordered[::-1])) - int(''.join(ordered))


def test0():
    s = [1, 31, 3, 3132, 5]
    print(bigger_together(s))


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert bigger_together([1, 2, 3, 4]) == 3087, "4321 - 1234"
    assert bigger_together([1, 2, 3, 4, 11, 12]) == 32099877, "43212111 - 11112234"
    assert bigger_together([0, 1]) == 9, "10 - 01"
    assert bigger_together([100]) == 0, "100 - 100"
    print('Done! I feel like you good enough to click Check')


if __name__ == '__main__':
    tests = [test0, test1]
    for test in tests:
        test()
