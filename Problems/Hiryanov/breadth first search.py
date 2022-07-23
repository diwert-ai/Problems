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
           12: {0, 11, 8},
           13: {7, 5},
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
           'c': {'d', 'g'},
           'd': {'c', 'h'},
           'e': {'a', 'f'},
           'f': {'g'},
           'g': {'f'},
           'h': {'d', 'g'}},
          {0: {1},
           1: {2, 3},
           2: {0},
           3: {}}]


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
    pass


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
