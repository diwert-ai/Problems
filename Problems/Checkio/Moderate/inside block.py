# https://py.checkio.org/en/mission/inside-block/

from typing import Tuple

signature = lambda p1, p2, q: (q[0]-p1[0])*(p2[1]-p1[1]) - (q[1]-p1[1])*(p2[0]-p1[0])


def in_triangle(t, p):
    s = signature(t[0], t[1], p), signature(t[1], t[2], p), signature(t[2], t[0], p)
    return all([r >= 0 for r in s]) or all([r <= 0 for r in s])


def square(polygon):
    ret = 0
    n = len(polygon)
    for i in range(n-1):
        det = polygon[i][0]*polygon[i+1][1] - polygon[i+1][0]*polygon[i][1]
        ret += det
    ret += polygon[n-1][0]*polygon[0][1]-polygon[0][0]*polygon[n-1][1]

    return 0.5*abs(ret)


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    n = len(polygon)
    if n == 3:
        return in_triangle(polygon, point)
    s = square(polygon)
    for i in range(n):
        reduced_polygon = tuple(polygon[ii] for ii in range(n) if ii != i)
        if square(reduced_polygon) > s:
            continue
        k = (i+1) % n
        t = polygon[i-1], polygon[i], polygon[k]
        good_triangle = True
        for j in range(n-3):
            if in_triangle(t, polygon[(k+j+1) % n]):
                good_triangle = False
                break
        if not good_triangle:
            continue
        if in_triangle(t, point):
            return True
        else:
            return is_inside(reduced_polygon, point)
    return False


if __name__ == '__main__':
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (2, 2)) is True, "First"
    assert is_inside(((1, 1), (1, 3), (3, 3), (3, 1)),
                     (4, 2)) is False, "Second"
    assert is_inside(((1, 1), (4, 1), (2, 3)),
                     (3, 2)) is True, "Third"
    assert is_inside(((1, 1), (4, 1), (1, 3)),
                     (3, 3)) is False, "Fourth"
    assert is_inside(((2, 1), (4, 1), (5, 3), (3, 4), (1, 3)),
                     (4, 3)) is True, "Fifth"
    assert is_inside(((2, 1), (4, 1), (3, 2), (3, 4), (1, 3)),
                     (4, 3)) is False, "Sixth"
    assert is_inside(((1, 1), (3, 2), (5, 1), (4, 3), (5, 5), (3, 4), (1, 5), (2, 3)),
                     (3, 3)) is True, "Seventh"
    assert is_inside(((1, 1), (1, 5), (5, 5), (5, 4), (2, 4), (2, 2), (5, 2), (5, 1)),
                     (4, 3)) is False, "Eighth"
    assert is_inside(((5, 3), (3, 3), (3, 1), (2, 1), (2, 4), (6, 4), (6, 1), (5, 1)),
                     (4, 2)) is False, "Nineth"

    print("All done! Let's check now")
