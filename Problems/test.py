﻿from collections import deque


def bfs_p(start_vertex, G, parents):
    queue = deque([start_vertex])
    parents[start_vertex] = None
    while queue:
        cur_v = queue.popleft()
        for neighbor in G[cur_v]:
            if neighbor not in parents:
                parents[neighbor] = cur_v
                queue.append(neighbor)


def find_path(start_vertex, end_vertex, G):
    if start_vertex not in G:
        return None
    parents = dict()
    bfs_p(start_vertex, G, parents)
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
    G = dict()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == value:
                s = set()
                ij = ((i, j+1), (i, j-1), (i+1, j), (i-1, j))
                for l, k in ij:
                    if -1 < l < n and -1 < k < m and matrix[l][k] == value:
                        s.add((l, k))
                G[(i, j)] = s
    return find_path(first, second, G) is not None


if __name__ == '__main__':
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                     (3, 2), (0, 5)) == True, 'First example'
    assert can_pass(((0, 0, 0, 0, 0, 0),
                     (0, 2, 2, 2, 3, 2),
                     (0, 2, 0, 0, 0, 2),
                     (0, 2, 0, 2, 0, 2),
                     (0, 2, 2, 2, 0, 2),
                     (0, 0, 0, 0, 0, 2),
                     (2, 2, 2, 2, 2, 2),),
                     (3, 3), (6, 0)) == False, 'First example'