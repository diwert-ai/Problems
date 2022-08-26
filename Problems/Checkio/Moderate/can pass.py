# https://py.checkio.org/ru/mission/can-pass/
# Дана матрица с цифрами и координаты (строка и столбец) двух клеток
# с одинаковым значением. Вы можете перемещаться между соседними клетками
# с одинаковыми значениями по вертикали и горизонтали. Определите есть ли
# путь между двумя заданными клетками.
# Матрица представлена, как массив массивов с цифрами. Координаты представлены,
# как два числа: строка и столбец. Результат проверяется, как булево значение.
# Есть путь существует - True, иначе - False.
from collections import deque
from itertools import chain, product, starmap


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
    if start_vertex not in g:
        return None
    parents = dict()
    bfs_p(start_vertex, g, parents)
    if end_vertex not in parents:
        return None
    parent = parents[end_vertex]
    path = [end_vertex]
    while parent is not None:
        path.append(parent)
        parent = parents[parent]
    return path[::-1]


def can_pass(matrix, first, second):
    value = matrix[first[0]][first[1]]
    if value != matrix[second[0]][second[1]]:
        return False
    n = len(matrix)
    m = len(matrix[0])
    g = dict()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == value:
                s = set()
                ij = ((i, j + 1), (i, j - 1), (i + 1, j), (i - 1, j))
                for p, k in ij:
                    if -1 < p < n and -1 < k < m and matrix[p][k] == value:
                        s.add((p, k))
                g[(i, j)] = s
    return find_path(first, second, g) is not None


# best clear solution
# ref: https://py.checkio.org/mission/can-pass/publications/gyahun_dash/python-3/itertools/
def can_pass_clear(matrix, first, second):
    digit = matrix[first[0]][first[1]]
    cells = product(range(len(matrix)), range(len(matrix[0])))
    living = {(y, x) for y, x in cells if matrix[y][x] == digit}

    neighbors = lambda y, x: ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1))
    tips = {first}
    while tips:
        tips = set(chain.from_iterable(starmap(neighbors, tips))) & living
        living -= tips
        if second in tips:
            return True

    return False


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 2), (0, 5)) is True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                    (3, 3), (6, 0)) is False, 'First example'
    print('All done!')
