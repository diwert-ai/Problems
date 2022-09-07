# https://py.checkio.org/en/mission/find-enemy/
from collections import deque


# noinspection SpellCheckingInspection
class HexGrid:
    letters = 'abABCDEFGHIJKLMNOPQRSTUVWXYZz'
    digits = '0123456789#'
    relative_dirs = {0: 'F', 1: 'R', 2: 'R', 3: 'B', 4: 'L', 5: 'L'}
    north_offset = {'N': 0, 'NE': 1, 'SE': 2, 'S': 3, 'SW': 4, 'NW': 5}
    graph = None

    @classmethod
    def init_graph(cls):
        g = dict()
        n, m = len(cls.letters), len(cls.digits)
        for i in range(n):
            for j in range(m):
                s = set()
                ij = [(i, j-1), (i+1, j), (i, j+1), (i-1, j)]
                ij = ij + [(i+1, j+1), (i-1, j+1)] if i % 2 else ij + [(i+1, j-1), (i-1, j-1)]
                for k, l in ij:
                    if -1 < k < n and -1 < l < m:
                        s.add(cls.letters[k]+cls.digits[l])
                g[cls.letters[i]+cls.digits[j]] = s
        cls.graph = g

    @classmethod
    def relative_index_for_north(cls, you, neighbor):
        i, j = cls.letters.index(you[0]), cls.digits.index(you[1])
        v, w = cls.letters.index(neighbor[0]),  cls.digits.index(neighbor[1])
        if i % 2:
            ix = [(i, j - 1), (i + 1, j), (i + 1, j + 1), (i, j + 1), (i - 1, j + 1), (i - 1, j)]
        else:
            ix = [(i, j - 1), (i + 1, j - 1), (i + 1, j), (i, j + 1), (i - 1, j), (i - 1, j - 1)]
        return ix.index((v, w))

    @classmethod
    def relative_direction(cls, you, enemy, direction):
        dist = len(find_path(you, enemy, cls.graph))
        dir_on_enemy = None
        path_fields = []
        for neighbor in cls.graph[you]:
            if len(find_path(neighbor, enemy, cls.graph)) == dist - 1:
                path_fields.append(neighbor)
        if len(path_fields) == 1:
            index = (cls.relative_index_for_north(you, path_fields[0]) - cls.north_offset[direction]) % 6
            dir_on_enemy = cls.relative_dirs[index]
        else:
            index0 = (cls.relative_index_for_north(you, path_fields[0]) - cls.north_offset[direction]) % 6
            index1 = (cls.relative_index_for_north(you, path_fields[1]) - cls.north_offset[direction]) % 6
            d_set = {cls.relative_dirs[index0],  cls.relative_dirs[index1]}
            if d_set in ({'R', 'F'}, {'L', 'F'}):
                dir_on_enemy = 'F'
            elif d_set == {'R'}:
                dir_on_enemy = 'R'
            elif d_set in ({'R', 'B'}, {'L', 'B'}):
                dir_on_enemy = 'B'
            elif d_set == {'L'}:
                dir_on_enemy = 'L'

        return [dir_on_enemy, dist-1]


def bfs_p(start_vertex, g, parents):
    queue = deque([start_vertex])
    parents[start_vertex] = None
    while queue:
        cur_v = queue.popleft()
        for neighbor in g[cur_v]:
            if neighbor not in parents:
                parents[neighbor] = cur_v
                queue.append(neighbor)


def find_path(start_vertex, end_vertex, g):
    parents = dict()
    bfs_p(start_vertex, g, parents)
    parent = parents[end_vertex]
    path = [end_vertex]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]


def find_enemy(you, direction, enemy):
    return HexGrid.relative_direction(you, enemy, direction)


def test0():
    tests = [("C3", "SE", "A1"), ("A1", "SW", "Z9")]
    for you, direct, enemy in tests:
        print(f'{you} {direct} {enemy} {find_enemy(you, direct, enemy)}')


def test1():
    assert find_enemy('G5', 'N', 'G4') == ['F', 1], "N-1"
    assert find_enemy('G5', 'N', 'I4') == ['R', 2], "NE-2"
    assert find_enemy('G5', 'N', 'J6') == ['R', 3], "SE-3"
    assert find_enemy('G5', 'N', 'G9') == ['B', 4], "S-4"
    assert find_enemy('G5', 'N', 'B7') == ['L', 5], "SW-5"
    assert find_enemy('G5', 'N', 'A2') == ['L', 6], "NW-6"
    assert find_enemy('G3', 'NE', 'C5') == ['B', 4], "[watch your six!]"
    assert find_enemy('H3', 'SW', 'E2') == ['R', 3], "right"
    assert find_enemy('A4', 'S', 'M4') == ['L', 12], "true left"


if __name__ == '__main__':
    HexGrid.init_graph()
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
