# Алгоритм Дейкстры поиск кртчайшего пути в графе с весами
# из лекции курса Хирьянова:
# https://www.youtube.com/watch?v=2N6YbTc-USw&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=25


# алгоритм bfs с перезажиганием
# веса - положительные числа.
# ассимптотика - O(N^2) по времени

from collections import deque


Graphs = [{1: {2: 2, 9: 15},
           2: {1: 2, 3: 1, 4: 5},
           3: {2: 1, 4: 3, 5: 1, 6: 2},
           4: {2: 5, 3: 3, 6: 4, 7: 6},
           5: {3: 1, 6: 1},
           6: {3: 2, 4: 4, 5: 1, 7: 7, 9: 3},
           7: {4: 6, 6: 7, 8: 2},
           8: {7: 2, 9: 12},
           9: {1: 15}},
          {'a': {'b': 11, 'd': 2, 'c': 0.1},
           'b': {'a': 11, 'c': 10},
           'c': {'b': 10, 'd': 1, 'e': 12, 'f': 7, 'a': 0.1},
           'd': {'a': 2, 'c': 1, 'f': 5},
           'e': {'c': 12, 'f': 5},
           'f': {'c': 7, 'e': 5, 'd': 5}}]


# weightes bfs with distances
def wbfs_d(start_vertex, G, distances):
    distances[start_vertex] = 0
    queue = deque([start_vertex])
    while queue:
        v = queue.popleft()
        for u in G[v]:
            if u not in distances or distances[v] + G[v][u] < distances[u]:
                distances[u] = distances[v] + G[v][u]
                queue.append(u)


def find_shortest_path(start, end, G):
    distances = dict()
    wbfs_d(start, G, distances)
    if end not in distances:
        return None
    path = [end]
    queue = deque([end])
    while queue:
        v = queue.popleft()
        for u in G[v]:
            if distances[u] + G[v][u] == distances[v]:
                path.append(u)
                queue.append(u)
                break
    return path[::-1]


def test0():
    bounds = ((1, 8), ('a', 'e'))
    for (start, end), G in zip(bounds, Graphs):
        distances = dict()
        wbfs_d(start, G, distances)
        print(f'shortest dists from {start}: {distances}')
        print(f'shortest path from {start} to {end}: ' +
              f'{find_shortest_path(start, end, G)}')


if __name__ == '__main__':
    test0()
