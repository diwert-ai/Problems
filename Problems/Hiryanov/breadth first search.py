﻿# обход графа в ширину - breadth first search, BFS
# из курса Хирьянова:
# https://www.youtube.com/watch?v=S-hjsamsK8U&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=24

# BFS можно применять:
# 1. Выделение компонент связности в графе за O(N+M)
# 2. Поиск кратчайшего пути в невзвешенном графе
# 3. Восстановление кратчайшего пути
# 4. Нахождение кратчайшего цикла в орграфе
# 5. Найти все ребра, лежащие на каком-либо кратчайшем пути
# между заданной парой вершин (a, b)
# 6. Найти все вершины, лежащие на каком-либо кратчайгем пути
# между заданной парой вершин (a, b)
# 7. Найти кратчайший четный путь в графе (т.е. путь четной длины)

# обход делается с привлечением очереди для
# правильного порядка обхода вершин

from collections import deque


# функция вычисляющая расстояния от start_vertex
# до всех вершин графа G
def bfs_dist(start_vertex, G, distances):
    # расстояние до себя же равно 0
    distances[start_vertex] = 0
    # создаем очередь
    queue = deque([start_vertex])
    # пока очередь не пуста
    while queue:
        # достаем первый элемент
        cur_v = queue.popleft()
        # проходим всех его соседей
        for neighbor in G[cur_v]:
            # если расстояние до соседа еще не вычислено
            if neighbor not in distances:
                # считаем расстояние до соседа
                distances[neighbor] = distances[cur_v] + 1
                # добавляем соседа в очередь чтобы проверить и его соседей
                queue.append(neighbor)


def test0():
    G = {0: {1, 11, 12},
         1: {0, 7},
         2: {6},
         3: {11},
         4: {10, 6},
         5: {8, 13},
         6: {2, 10, 4},
         7: {1, 13},
         8: {12, 5},
         9: {11},
         10: {6, 0},
         11: {0, 12, 14, 3, 9},
         12: {0, 11, 8},
         13: {7, 5},
         14: {11}}

    distances = dict()  # словарь расстояний
    bfs_dist(0, G, distances)
    print(f'dists for vertex 0: {distances}')

if __name__ == '__main__':
    test0()
