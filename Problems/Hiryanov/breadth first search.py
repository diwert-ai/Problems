# обход графа в ширину - breadth first search, BFS
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

Graphs = [{0: {1, 11, 12},
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
           12: {0, 11, 8, 13},
           13: {7, 5, 12},
           14: {11}},
          {0: {18, 1, 14},
           1: {0, 14, 15},
           2: {1, 15, 17},
           3: {7},
           4: {6, 5},
           5: {4},
           6: {4},
           7: {3, 9, 8},
           8: {7},
           9: {7, 10},
           10: {11, 9},
           11: {10},
           12: {13},
           13: {12},
           14: {16, 15, 0, 1},
           15: {1, 14, 2},
           16: {14},
           17: {2},
           18: {0}},
          {'A': {'B'},
           'B': {'C', 'D'},
           'C': {'A'},
           'D': {'E'},
           'F': {'D'},
           'E': {'F'},
           'G': {'F', 'H'},
           'H': {'I'},
           'I': {'J'},
           'J': {'G'},
           'K': {'J'}},
          {'A': {'B'},
           'B': {'C', 'D'},
           'C': {'E'},
           'D': {},
           'E': {'D', 'F'},
           'F': {'G'},
           'G': {'E', 'H'},
           'H': {}},
          {'A': {'B', 'D'},
           'B': {'C', 'E'},
           'C': {'A', 'D'},
           'D': {'E', 'K'},
           'E': {'C', 'H'},
           'F': {'E', 'H', 'J'},
           'G': {'F', 'J'},
           'H': {'G'},
           'J': {'E'},
           'K': {'J'},
           'L': {'J', 'K'}},
          {'a': {'b'},
           'b': {'c', 'e', 'f'},
           'c': {'g'},
           'd': {'c', 'h'},
           'e': {'a', 'f'},
           'f': {},
           'g': {'f'},
           'h': {'g'}},
          {0: {1},
           1: {2, 3},
           2: {0},
           3: {}},
          {'a': {'b', 'c', 'd'},
           'b': {'a', 'e'},
           'c': {'a', 'e'},
           'd': {'a', 'e'},
           'e': {'b', 'c', 'd', 'f', 'g', 'h'},
           'f': {'e', 'j'},
           'g': {'e', 'j'},
           'h': {'e', 'j'},
           'j': {'f', 'g', 'h'}},
          {1: {2},
           2: {3, 5},
           3: {4},
           4: {},
           5: {6},
           6: {4}}]


# функция вычисляющая расстояния от start_vertex
# до всех вершин графа G
def bfs_d(start_vertex, G, distances):
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
    for G in Graphs:
        distances = dict()  # словарь расстояний
        if 0 not in G:
            continue
        bfs_d(0, G, distances)
        print(f'dists for vertex 0: {distances}')
    print('')


# bfs для подсчета компонент связности
def bfs_c(vertex, G, used):
    used.add(vertex)
    queue = deque([vertex])
    print(vertex, end=' ')
    while queue:
        cur_v = queue.popleft()
        for neighbor in G[cur_v]:
            if neighbor not in used:
                print(neighbor, end=' ')
                used.add(neighbor)
                queue.append(neighbor)


# процедура подсчета компонент связности
def n_comp(G):
    N = 0
    used = set()
    for vertex in G:
        if vertex not in used:
            print(f'comp #{N}: ', end='')
            bfs_c(vertex, G, used)
            print('')
            N += 1
    return N


def test1():
    for i, G in enumerate(Graphs):
        print(f'graph #{i} num components: {n_comp(G)}')
        print('')


# bfs для поиска кратчайшего пути
def bfs_p(start_vertex, G, parents):
    queue = deque([start_vertex])
    parents[start_vertex] = None
    while queue:
        cur_v = queue.popleft()
        for neighbor in G[cur_v]:
            if neighbor not in parents:
                parents[neighbor] = cur_v
                queue.append(neighbor)


# поиск кратчайшего пути
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


def test2():
    for i, G in enumerate(Graphs):
        start_vertex = 'A'
        end_vertex = 'F'
        print(f'[graph #{i}] from {start_vertex} to {end_vertex} path: ' +
              f'{find_path(start_vertex, end_vertex, G)}')
    print('')


# задача о шахматном коне
# по каким клеткам должен пройти конь,
# чтобы попасть из a8 в h1

def knight_graph():
    G = dict()
    digits = '12345678'
    letters = 'abcdefgh'
    for i in range(8):
        for j in range(8):
            s = set()
            ij = ((i+2, j+1), (i+2, j-1), (i-2, j+1), (i-2, j-1),
                  (i+1, j+2), (i+1, j-2), (i-1, j+2), (i-1, j-2))
            for k, l in ij:
                if -1 < k < 8 and -1 < l < 8:
                    s.add(letters[k]+digits[l])
            G[letters[i]+digits[j]] = s
    return G


def test3():
    G = knight_graph()
    start = 'a8'
    end = 'h1'
    print(f'from {start} to {end} knight path is: {find_path(start, end, G)}')
    print('')


# нахождение кратчайшего цикла
# в орграфе (для обычного графа
# будет возвращать элементарный
# цикл длины 2 - т.е. ребро)
# ref: http://e-maxx.ru/algo/bfs
# производим поиск в ширину из каждой вершины;
# как только в процессе обхода мы пытаемся
# пойти из текущей вершины по какому-то ребру
# в уже посещённую вершину, то это означает,
# что мы нашли кратчайший цикл, и останавливаем
# обход в ширину; среди всех таких найденных циклов
# (по одному от каждого запуска обхода) выбираем кратчайший.
def bfs_cycle(vertex, G, used):
    used.add(vertex)
    queue = deque([vertex])
    while queue:
        cur_v = queue.popleft()
        for neighbor in G[cur_v]:
            if neighbor not in used:
                used.add(neighbor)
                queue.append(neighbor)
            else:
                return neighbor, cur_v
    return (None, None)


def shortest_cycle(G):
    shortest_cycle = None
    for vertex in G:
        used = set()
        cycle_start, cycle_end = bfs_cycle(vertex, G, used)
        if cycle_start is not None:
            cycle_path = find_path(cycle_start, cycle_end, G)
            if cycle_path is not None:
                if (shortest_cycle is None or
                        len(cycle_path) < len(shortest_cycle)):
                    shortest_cycle = cycle_path
    return shortest_cycle


def test4():
    for i, G in enumerate(Graphs):
        print(f'shortest cycle of graph #{i} is: {shortest_cycle(G)}')
    print('')


# ref: http://e-maxx.ru/algo/bfs
# нахождение всех вершин и всех ребер
# на каком-либо кратчайшем пути из a в b.
# Для этого надо запустить 2 поиска в ширину:
# из a, и из b. Обозначим через d_a[] массив
# кратчайших расстояний, полученный в результате
# первого обхода, а через d_b[] — в результате
# второго обхода. Теперь для любой вершины v
# легко проверить, лежит ли он на каком-либо
# кратчайшем пути: критерием будет условие
# d_a[v] + d_b[v] = d_a[b].
def all_verts(a, b, G):
    all_v = []
    d_a = dict()
    d_b = dict()
    bfs_d(a, G, d_a)
    bfs_d(b, G, d_b)
    for v in G:
        if v in d_a and v in d_b and d_a[v] + d_b[v] == d_a[b]:
            all_v.append(v)
    return all_v


# ref: http://e-maxx.ru/algo/bfs
# Найти все рёбра, лежащие на каком-либо кратчайшем
# пути между заданной парой вершин (a,b). Для этого
# надо запустить 2 поиска в ширину: из a, и из b.
# Обозначим через d_a[] массив кратчайших расстояний,
# полученный в результате первого обхода, а через d_b[]
# — в результате второго обхода. Теперь для любого ребра
# (u,v) легко проверить, лежит ли он на каком-либо
# кратчайшем пути: критерием будет условие
# d_a[u] + 1 + d_b[v] = d_a[b].
def all_edges(a, b, G):
    all_e = []
    d_a = dict()
    d_b = dict()
    bfs_d(a, G, d_a)
    bfs_d(b, G, d_b)
    for u in G:
        for v in G[u]:
            if (u in d_a and u in d_b and v in d_a and v in d_b and
                    d_a[u] + 1 + d_b[v] == d_a[b]):
                all_e.append((u, v))
    return all_e


# ref: http://e-maxx.ru/algo/bfs
# Найти кратчайший чётный путь в графе (т.е. путь чётной длины).
# Для этого надо построить вспомогательный граф, вершинами которого
# будут состояния (v,c), где v — номер текущей вершины,
# c = 0...1 — текущая чётность. Любое ребро (a,b) исходного графа
# в этом новом графе превратится в два ребра ((u,0),(v,1)) и ((u,1),(v,0)
# После этого на этом графе надо обходом в ширину найти кратчайший путь
# из стартовой вершины в конечную, с чётностью, равной 0.
def find_even_path(start, end, G):
    H = dict()
    for g in G:
        H[(g, 0)] = set()
        H[(g, 1)] = set()

    for u in G:
        for v in G[u]:
            H[(u, 0)].add((v, 1))
            H[(u, 1)].add((v, 0))
    return find_path((start, 0), (end, 0), H)


def test5():
    start = 'a'
    end = 'j'
    for i, G in enumerate(Graphs):
        if start in G and end in G:
            print(f'all vertexes between {start} and {end} in graph #{i}:' +
                  f'{all_verts(start, end, G)}')
            print(f'all edges between {start} and {end} in graph #{i}:' +
                  f'{all_edges(start, end, G)}')
    print('')


def test6():
    start = 1
    end = 4
    for i, G in enumerate(Graphs):
        if start in G and end in G:
            print(f'[graph #{i}] from {start} to {end} even path: ' +
                  f'{find_even_path(start, end, G)}')

if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
