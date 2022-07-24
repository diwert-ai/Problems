# https://py.checkio.org/en/mission/inside-block/

# Вершины соединены последовательно и последняя соединена с первой.
# Также даны координаты точки для проверки. Вам нужно определить находится
# ли точка внутри многоугольника. Если точка лежит на стороне многоугольника,
# то считаем, что точка внутри.

from typing import Tuple

signature = lambda p1, p2, q: (q[0]-p1[0])*(p2[1]-p1[1]) - (q[1]-p1[1])*(p2[0]-p1[0])


def in_triangle(t, p):
    s = signature(t[0], t[1], p), signature(t[1], t[2], p), signature(t[2], t[0], p)
    return all([r >= 0 for r in s]) or all([r <= 0 for r in s])


def oriented_area(polygon):
    ret = 0
    n = len(polygon)
    for i in range(n-1):
        det = polygon[i][0]*polygon[i+1][1] - polygon[i+1][0]*polygon[i][1]
        ret += det
    ret += polygon[n-1][0]*polygon[0][1]-polygon[0][0]*polygon[n-1][1]
    return ret


def is_inside(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int], s=None) -> bool:
    n = len(polygon)
    if n == 3:
        return in_triangle(polygon, point)
    s = s or oriented_area(polygon)
    for i in range(n):
        k = (i+1) % n
        ear = polygon[i-1], polygon[i], polygon[k]
        if abs(s-oriented_area(ear)) > abs(s):
            continue
        good_ear = True
        for j in range(n-3):
            if in_triangle(ear, polygon[(k+j+1) % n]):
                good_ear = False
                break
        if not good_ear:
            continue
        if in_triangle(ear, point):
            return True
        return is_inside(polygon[:i]+polygon[i+1:], point, s)
    return False


def is_inside_false(polygon: Tuple[Tuple[int, int], ...], point: Tuple[int, int]) -> bool:
    n = len(polygon)
    if n == 3:
        return in_triangle(polygon, point)

    for i in range(n):
        k = (i+1) % n
        t = polygon[i-1], polygon[i], polygon[k]
        good_triangle = True

        for j in range(n-3):
            if in_triangle(t, polygon[(k+j+1) % n]):
                good_triangle = False
                break

        if good_triangle:
            if in_triangle(t, point):
                return True
            else:
                new_polygon = tuple(polygon[ii] for ii in range(n) if ii != i)
                return is_inside(new_polygon, point)
    return False


# best clear solution
# ref: https://py.checkio.org/mission/inside-block/publications/Sim0000/python-3/second/?ordering=most_voted&filtering=all
def is_inside_clear(polygon, point):
    x, y, x1, y1 = point + polygon[-1]
    count = 0
    for x2, y2 in polygon:
        if y1 == y2:
            if y == y1 and min(x1, x2) <= x <= max(x1, x2):
                return True  # on line
        else:
            cx = x1 + (x2 - x1) * (y - y1) / (y2 - y1)  # x of cross point
            if x == cx:
                return True  # on line
            if x < cx and min(y1, y2) <= y < max(y1, y2):
                count += 1
        x1, y1 = x2, y2
    return count % 2 == 1  # odd then inside


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
                     (4, 2)) is False, "Ninth"
    assert is_inside(((2, 5), (2, 2), (5, 2), (1, 1)),
                     (3, 3)) is False, "Tenth"

    print("All done! Let's check now")

