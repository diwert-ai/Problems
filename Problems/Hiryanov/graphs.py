# структуры данных для графов
# из лекции Хирьянова
# https://www.youtube.com/watch?v=rg7DX6U0v9k&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=22
# размер V (кол-во вершин) = N порядок графа
# размер E (кол-во  ребер) = M размер графа

# структуры для хранения графов

# 1 вариант.
# два множества - вершин и ребер.


# проверка на смежность двух вершин требует O(1) времени
def get_adjacent_vertices(G):
    V, E = G
    for i in V:
        for j in V:
            if i != j:
                print(f'{(i,j)} is edge') if (i, j) in E or (j, i) in E \
                    else print(f'{(i,j)} is not edge')
    print('')


# в такой структуре данных поиск всех соседних вершин требует О(N) времени
def get_neighbors(G, v):
    V, E = G
    print(f'find neigbors of {v}...')
    for i in V:
        if (v, i) in E or (i, v) in E:
            print(f'{i} is neighbor {v}')
    print('')


def test0():
    V = {'A', 'B', 'C', 'D'}  # вершины
    E = {('A', 'B'), ('B', 'C'), ('C', 'D')}  # ребра
    G = (V, E)  # граф

    get_adjacent_vertices(G)
    for v in V:
        get_neighbors(G, v)

# 2 вариант.
# матрица смежности + массив вершин и словарь index для
# быстрого вычисления номера вершины по названию


# проверка на смежность двух вершин в такой структуре требует тоже O(1) времени
def get_adjacent_vertices_A(G):
    V, index, A = G
    for v0 in V:
        for v1 in V:
            print(f'{(v0, v1)} is edge') if A[index[v0]][index[v1]] \
                else print(f'{(v0, v1)} is not edge')
    print('')


# поиск соседей в матрице смежности по прежнему за О(N)
def get_neighbors_A(G, v):
    V, index, A = G
    print(f'find neigbors of {v}...')
    for i, a in enumerate(A[index[v]]):
        if a > 0:
            print(f'{V[i]} is neighbor {v}')
    print('')


def test1():
    # хотим чтобы у вершин был номер, поэтому создаем list
    V = ['A', 'B', 'C', 'D']
    # для быстрого вычисления индекса (за O(1)) создаем словарь
    index = {V[i]: i for i in range(len(V))}
    # матрица смежности: - i строки и j столбцы - это вершины,
    # если i,j ребро существует,
    # то a_{ij} = 1 (либо n, если ребро кратное),
    # если не существует, то a_{ij} = 0.
    # в такой структуре можно хранить не только простые графы
    # (без кратных ребер) как в варианте 1.
    # для неориентированного графа матрица симметрична.
    A = [[0, 1, 0, 0],
         [1, 0, 1, 0],
         [0, 1, 0, 1],
         [0, 0, 1, 0]]
    G = (V, index, A)  # граф

    get_adjacent_vertices_A(G)
    for v in V:
        get_neighbors_A(G, v)

# 3 вариант.
# списки смежности задаются одним словарем множеств
# смежных вершин (в тч пустых) для каждой вершины


# проверка на смежность двух вершин в такой структуре
# требует также O(1) времени
def get_adjacent_vertices_G(G):
    for v0 in G:
        for v1 in G:
            print(f'{(v0, v1)} is edge') if v1 in G[v0] \
                else print(f'{(v0, v1)} is not edge')
    print('')


# поиск соседей вершины в списках смежности требует О(K)
# времени - где K число соседей,
# т.е. максимально быстро.
def get_neighbors_G(G, v):
    for n in G[v]:
        print(f'{n} is neighbor {v}')
    print('')


def test2():
    G = {'A': {'B'},
         'B': {'A', 'C'},
         'C': {'B', 'D'},
         'D': {'C'}}

    get_adjacent_vertices_G(G)
    for v in G:
        get_neighbors_G(G, v)


# пример считывания данных с консоли
def test3():
    # матрица смежности
    M, N = (int(x) for x in input().split())
    V = []
    index = {}
    A = [[0]*N for i in range(N)]

    for i in range(N):
        v1, v2 = input().split()
        for v in v1, v2:
            if v not in index:
                V.append(v)
                index[v] = len(V)-1
        A[index[v1]][index[v2]] = 1
        A[index[v2]][index[v1]] = 1
    print(V)
    print(index)
    print(A)

    # списки смежности
    G = {}
    for i in range(N):
        v1, v2 = input().split()
        for v, u in (v1, v2), (v2, v1):
            if v not in G:
                G[v] = {u}
            else:
                G[v].add(u)
    print(G)


# компактное хранение списков смежности для неизменяемого графа
# храним только индексы вершин:
# 0: 1
# 1: 0, 2, 3
# 2: 1, 3
# 3: 1, 2, 4
# 4: 3
def test4():
    # объеденные списки соседей 
    edges = [1, 0, 2, 3, 1, 3, 1, 2, 4, 3]
    offset = [0, 1, 4, 6, 9, 10]
    # offset смещения в edges для начала списка соседей каждой вершины
    # последнее значение фиктивное - правая граница последнего списка смежности
    # список смежности i вершины: edges[offset[i]:offset[i+1]]

    for v in range(len(offset)-1):
        print(f'vertex {v}: {edges[offset[v]:offset[v+1]]}')


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
