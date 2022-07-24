# Алгоритм Флойда-Уоршелла. WFI
# Из лекции Хирьянова:
# https://www.youtube.com/watch?v=2N6YbTc-USw&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=25

# Нахождение кратчайших путей сразу для всех вершин
# (от каждой к каждой) взвешенного графа.
# Требует О(N^3) времени.
# Тип: динамическое программирование.
# работает с отрицательными весами, но
# не циклами отрицательного веса.

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

# пусть F_{i,j}^{0} - кратчайшее расстояние от вершины i к
# вершине j в графе G при условии, что нельзя пользоваться
# другим промежуточными вершинами. F_{i,j}^{1} - можно
# пользоваться 1й промежуточной вершиной . F_{i,j}^{k} -
# можно пользоваться первыми k штук вершин.
# Тогда F_{i,j}^{k} = min (F_{i,j}^{k-1}, F_{i,k}^{k-1} + F_{k,j}^{k-1})
# Ответ будет находиться в матрице F_{i,j}^{N} где N число вершин в G.


# g_order - упорядоченный список вершин G
# (для того чтобы алгоритм работал в т.ч., когда вершины
# имееют буквенные названия)
# в начале F[i][i] считаем 0, остальные расстояни +inf
def wfi(G, g_order):
    N = len(G)
    F = [[0 if i == j else float('inf') for i in range(N)] for j in range(N)]
    for i, v in enumerate(g_order):
        for j, u in enumerate(g_order):
            if u in G[v]:
                F[i][j] = G[v][u]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                F[i][j] = min(F[i][j], F[i][k]+F[k][j])
    return F


def find_shortest_path(start, end, G):
    g_order = []
    for v in G:
        g_order.append(v)
    F = wfi(G, g_order)
    i_start = g_order.index(start)
    distances = {g: F[i_start][g_order.index(g)] for g in g_order}
    if distances[end] == float('inf'):
        return None, distances
    path = [end]
    queue = deque([end])
    while queue:
        v = queue.popleft()
        for u in G[v]:
            if distances[u] + G[v][u] == distances[v]:
                path.append(u)
                queue.append(u)
                break
    return path[::-1], distances


def test0():
    bounds = ((1, 8), ('a', 'e'))
    for (start, end), G in zip(bounds, Graphs):
        path, dists = find_shortest_path(start, end, G)
        print(f'shortest path from {start} to {end}: {path}')
        print(f'distance from {start} to {end}: {dists[end]}')
        print(f'distances from {start} to vertexes: {dists}')


if __name__ == '__main__':
    test0()
