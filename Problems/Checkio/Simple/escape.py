# https://py.checkio.org/ru/mission/escape/

from typing import List


def escape(jar: List[int], fly: List[int]) -> bool:
    w, h, d = jar
    x0, y0, vx0, vy0 = fly

    def collision_state(x, y, vx, vy):
        tx = ((w - x) / vx if vx > 0 else -x / vx) if vx else float('inf')
        ty = ((h - y) / vy if vy > 0 else -y / vy) if vy else float('inf')

        if tx < ty:
            return w if vx > 0 else 0, y + vy * tx, -vx, vy
        elif tx == ty:
            return w if vx > 0 else 0, h if vy > 0 else 0, -vx, -vy
        else:
            return x + vx * ty, h if vy > 0 else 0, vx, -vy
    for i in range(20):
        x0, y0, vx0, vy0 = collision_state(x0, y0, vx0, vy0)
        if (w - d) / 2 < x0 < (w + d) / 2 and y0 == h:
            return True
    return False


def test0():
    print(escape([1000, 1000, 200], [250, 250, -10, -50]))


def test1():
    print("Example:")
    print(escape([1000, 500, 200], [0, 0, 100, 0]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert escape([1000, 500, 200], [0, 0, 100, 0]) is False
    assert escape([1000, 500, 200], [450, 50, 0, -100]) is True
    assert escape([1000, 1000, 200], [450, 1000, 100, 0]) is False
    assert escape([1000, 1000, 200], [250, 250, -10, -50]) is False
    assert escape([1000, 2000, 200], [20, 35, 100, 175]) is True
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
