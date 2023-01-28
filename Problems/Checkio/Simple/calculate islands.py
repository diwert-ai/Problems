# https://py.checkio.org/ru/mission/calculate-islands/
#  Как обычно это двумерный массив, где все разбито на квадраты и 0 - это вода, 1 - земля.
#  Остров - это группа квадратов суши окруженных водой. Квадраты соединяются между собой
#  сторонами и углами. Необходимо подсчитать площадь каждого острова и вернуть список этих
#  площадей (сколько квадратов входит в остров) в возрастающем порядке. Все квадраты вне
#  карты - это вода.
from typing import List
from collections import deque


def checkio(land_map: List[List[int]]) -> List[int]:
    graph, used, result, n_rows, n_columns = dict(), set(), list(), len(land_map), len(land_map[0])

    def get_neighbors(i_row, j_col):
        neighbors = set()
        for di in (-1, 0, 1):
            for dj in (-1, 0, 1):
                if di != 0 or dj != 0:
                    ii, jj = i_row + di, j_col + dj
                    if -1 < ii < n_rows and -1 < jj < n_columns and land_map[ii][jj] == 1:
                        neighbors.add(f'{ii}{jj}')
        return neighbors

    def bfs(start_vertex):
        used.add(start_vertex)
        queue, num_vertices = deque([start_vertex]), 1
        while queue:
            current_vertex = queue.popleft()
            for neighbor in graph[current_vertex]:
                if neighbor not in used:
                    num_vertices += 1
                    used.add(neighbor)
                    queue.append(neighbor)

        return num_vertices

    for row in range(n_rows):
        for column in range(n_columns):
            if land_map[row][column]:
                graph[f'{row}{column}'] = get_neighbors(row, column)

    for vertex in graph:
        if vertex not in used:
            result.append(bfs(vertex))

    return sorted(result)


def test0():
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))
    pass


def test1():
    print("Example:")
    print(checkio([[0, 0, 0, 0, 0],
                   [0, 0, 1, 1, 0],
                   [0, 0, 0, 1, 0],
                   [0, 1, 0, 0, 0],
                   [0, 0, 0, 0, 0]]))

    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 0, 0, 0],
                    [0, 0, 0, 0, 0]]) == [1, 3], "1st example"
    assert checkio([[0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 0],
                    [0, 1, 1, 0, 0]]) == [5], "2nd example"
    assert checkio([[0, 0, 0, 0, 0, 0],
                    [1, 0, 0, 1, 1, 1],
                    [1, 0, 0, 0, 0, 0],
                    [0, 0, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0],
                    [0, 1, 1, 1, 1, 0],
                    [0, 0, 0, 0, 0, 0]]) == [2, 3, 3, 4], "3rd example"
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
