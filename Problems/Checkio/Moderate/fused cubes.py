# https://py.checkio.org/en/mission/fused-cubes/
# This is a mission to calculate the volume of objects that combines cubes.
#
# You are given a list of cube details (tuple of 4 integers: X coordinate, Y coordinate, Z coordinate, edge length).
#
# Each coordinate is the minimum value.
# All edges parallel to the coordinate axes.
# If the cube share the part of another cube or touch with the face of another cube, they are considered as one object.
# You should return a list (or iterable) of the volumes of all objects.
from collections import deque


class Parallelepiped:
    def __init__(self, x, y, z, lx, ly=None, lz=None):
        self.x, self.y, self.z = x, y, z
        self.lx = lx
        self.ly = ly if ly is not None else lx
        self.lz = lz if lz is not None else lx

    def volume(self):
        return self.lx * self.ly * self.lz

    def dims(self):
        return (self.lx > 0) + (self.ly > 0) + (self.lz > 0)

    def __mul__(self, other):
        x, y, z = max(self.x, other.x), max(self.y, other.y), max(self.z, other.z)
        dx = min(self.x + self.lx, other.x + other.lx) - x
        dy = min(self.y + self.ly, other.y + other.ly) - y
        dz = min(self.z + self.lz, other.z + other.lz) - z
        if dx < 0 or dy < 0 or dz < 0:
            dx, dy, dz = 0, 0, 0
        return Parallelepiped(x, y, z, dx, dy, dz)

    def __str__(self):
        return f'({self.x},{self.y},{self.z}) ({self.lx},{self.ly},{self.lz})'


def fused_cubes(cubes):
    answer, volumes, intersections, used, component_set, n = list(), dict(), dict(), set(), set(), len(cubes)

    for i in range(n):
        cube_i = Parallelepiped(*cubes[i])
        volumes[(i,)] = cube_i.volume()
        for j in range(i + 1, n):
            int_ij = cube_i * Parallelepiped(*cubes[j])
            v = int_ij.volume()
            if v > 0:
                volumes[(i, j)] = v
            intersections[frozenset((i, j))] = int_ij

    def fill_volumes(start_tpl):
        if len(start_tpl) == n:
            return
        start = start_tpl[-1] + 1
        for k in range(start, n):
            int_k = intersections[frozenset(start_tpl)] * Parallelepiped(*cubes[k])
            vl = int_k.volume()
            if vl > 0:
                new_tpl_index = start_tpl + (k,)
                intersections[frozenset(new_tpl_index)] = int_k
                volumes[new_tpl_index] = vl
                print(new_tpl_index, vl)
                fill_volumes(new_tpl_index)

    def neighbours(base_index):
        result = list()
        for k in range(n):
            if k != base_index:
                if intersections[frozenset((k, base_index))].dims() > 1:
                    result.append(k)
        return result

    def calc_component_volume():
        sum_volume, m = 0, len(component_set)
        print(f'm = {m}')

        for v_index in volumes:
            for k in v_index:
                if k in component_set:
                    sum_volume += volumes[v_index] * (-1) ** (len(v_index) + 1)
                    break

        return sum_volume

    def bfs_cubes(start_index):
        used.add(start_index)
        component_set.add(start_index)
        queue = deque([start_index])
        while queue:
            cur_index = queue.popleft()
            for neighbor_index in neighbours(cur_index):
                if neighbor_index not in used:
                    used.add(neighbor_index)
                    component_set.add(neighbor_index)
                    queue.append(neighbor_index)

    for vol in volumes.copy():
        if len(vol) == 2:
            fill_volumes(vol)

    for index in range(n):
        if index not in used:
            bfs_cubes(index)
            answer.append(calc_component_volume())
            print(component_set)
            component_set.clear()

    for vol in volumes:
        print(vol, volumes[vol])

    return answer


def test0():
    c1 = (0, 0, 0, 3)
    c2 = (1, 2, 2, 3)
    p1 = Parallelepiped(*c1)
    p2 = Parallelepiped(*c2)
    p = p1 * p2
    print(p)
    print(p1.volume() + p2.volume() - (p1 * p2).volume())
    print(sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])))

    cube_tests = [[(-1, 0, 0, 1),
                   (1, 0, 0, 1),
                   (0, 1, 0, 1),
                   (0, -1, 0, 1),
                   (0, 0, 1, 1),
                   (0, 0, -1, 1)],
                  ]

    for c_test in cube_tests:
        print(fused_cubes(c_test))

    c1 = (-1, 0, 0, 1)
    c2 = (1, 0, 0, 1)
    p1 = Parallelepiped(*c1)
    p2 = Parallelepiped(*c2)
    print(p1 * p2)

    print(fused_cubes(
        [(0, 0, -10, 1), (0, 0, -9, 1), (0, 0, -8, 1), (0, 0, -7, 1), (0, 0, -6, 1), (3, 0, -10, 1), (3, 0, -9, 1),
         (3, 0, -8, 1), (3, 0, -7, 1), (3, 0, -6, 1), (1, 4, -6, 2), (0, 0, -5, 2), (2, 0, -5, 2), (0, 1, -5, 2),
         (2, 1, -5, 2), (1, 3, -5, 2), (2, 0, -3, 2), (1, 2, -3, 2), (1, 1, -1, 2), (1, 0, 0, 2), (1, 0, 2, 2),
         (3, 0, 1, 1), (3, 0, 2, 1), (3, 0, 3, 1), (-9, 2, 6, 1), (-10, 0, 5, 2), (-9, 0, 5, 2), (-9, 0, 6, 2),
         (-11, 0, 4, 1), (-10, 0, 4, 1), (-9, 0, 4, 1), (-8, 0, 4, 1), (-7, 0, 4, 1), (-7, 0, 5, 1), (-7, 0, 6, 1),
         (-7, 0, 7, 1), (-7, 0, 8, 1), (-8, 0, 8, 1), (-11, 0, 5, 1)]))

    print(fused_cubes([(-9, 0, 0, 2), (-9, 2, 0, 2), (-5, 0, 1, 2),
                       (-5, 2, 1, 2), (-1, 0, 2, 2), (-1, 2, 2, 2),
                       (3, 0, 3, 2), (3, 2, 3, 2), (7, 0, 2, 2),
                       (7, 2, 2, 2), (6, 3, 2, 2), (4, 3, 2, 2),
                       (2, 3, 3, 2), (0, 3, 3, 2), (-2, 3, 2, 2),
                       (-4, 3, 2, 2), (-2, 0, -7, 2), (0, 0, 0, 1),
                       (0, 1, 0, 1), (3, 0, -1, 1), (3, 1, -1, 1)]))

    cubes = [(-4, -2, -2, 4), (-3, -3, -2, 4), (-3, -2, -3, 4), (-3, -2, -2, 4), (-3, -2, -1, 4), (-3, -1, -2, 4),
             (-2, -4, -2, 4), (-2, -3, -3, 4), (-2, -3, -2, 4), (-2, -3, -1, 4), (-2, -2, -4, 4), (-2, -2, -3, 4),
             (-2, -2, -2, 4), (-2, -2, -1, 4), (-2, -2, 0, 4), (-2, -1, -3, 4), (-2, -1, -2, 4), (-2, -1, -1, 4),
             (-2, 0, -2, 4), (-1, -3, -2, 4), (-1, -2, -3, 4), (-1, -2, -2, 4), (-1, -2, -1, 4), (-1, -1, -2, 4),
             (0, -2, -2, 4)]

    # print(fused_cubes(cubes))
    pr = Parallelepiped(*cubes[0])
    for i in (1, 2, 3, 4, 5, 6, 10, 15, 16, 20, 22, 23):
        pr = pr * Parallelepiped(*cubes[i])
        print(pr, pr.volume())


def test1():
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 2, 2, 3)])) == [52], 'fused'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 2, 3)])) == [54], 'touch with faces'
    assert sorted(fused_cubes([(0, 0, 0, 3), (1, 3, 3, 3)])) == [27, 27], 'touch with edges'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 3, 3, 3)])) == [27, 27], 'touch with vertices'
    assert sorted(fused_cubes([(0, 0, 0, 3), (3, 4, 3, 3)])) == [27, 27], 'separated'
    assert sorted(fused_cubes([(0, 0, 0, 3), (-2, -2, -2, 3)])) == [53], 'negative coordinates'
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
