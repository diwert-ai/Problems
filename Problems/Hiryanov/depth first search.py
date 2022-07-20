# обход графа в глубину Depth-First Search, DFS
# из лекции Хирьянова:
# https://www.youtube.com/watch?v=sBJ7ana1fgI&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=23

# позволяет:
# 1. выделить компоненту связности;
# 2. подсчитать кол-во компонент;
# 3. найти простой цикл (хотя бы один, если существует);
# 4. определить граф двудольный или нет (можно ли расскрасить
# вершины графа в 2 цвета так, что любое ребро соединяет
# только разноцветные вершины)
# 5. найти мосты и точки сочленения
# 6. c орграфами: выделение компонент сильной связности -
# делается 2 обхода в глубину - алгоритм Косарайю
# 7. топологическая сортировка


def dfs(vertex, G, used=None):
    used = used or set()
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs(neighbor, G, used)


def test0():
    G = {0: {18, 1, 14},
         1: {0, 14, 15},
         2: {1, 15, 17, 3},
         3: {2, 7, 4},
         4: {3, 6, 5},
         5: {4},
         6: {4},
         7: {3, 9, 8},
         8: {7},
         9: {7, 10},
         10: {11, 9, 12},
         11: {10},
         12: {13, 14, 11},
         13: {12},
         14: {16, 15, 0, 1},
         15: {1, 14, 2},
         16: {14},
         17: {2},
         18: {0}}
    print(f'traversal of the graph in depth: ', end='')
    dfs(0, G)
    print('')


# видоизмененная функция обхода для подсчета компонент связности
def dfs_c(vertex, G, used):
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs_c(neighbor, G, used)


def test1():
    G = {0: {18, 1, 14},
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
         18: {0}}

    used = set()
    N = 0
    for vertex in G:
        if vertex not in used:
            print(f'graph component #{N}: ', end='')
            dfs_c(vertex, G, used)
            print('')
            N += 1
    print(f'N = {N}')

# Алгоритм Косарайю выделения компонент сильной связности
# ориентированного графа. 
# Ориентированный граф (орграф) называется сильно связным
# (англ. strongly connected), если любые две его вершины
# s и t сильно связны, то есть если существует ориентированный
# путь из s в t и одновременно ориентированный путь из t в s.
def dfs_k():
    pass


def test2():
    G = {'A': {'B'},
         'B': {'C','D'},
         'C': {'A'},
         'D': {'E'},
         'F': {'D'},
         'E': {'F'},
         'G': {'F','H'},
         'H': {'I'},
         'I': {'J'},
         'J': {'G'},
         'K': {'J'}}
    used = set()
    N = 0
    for vertex in G:
        if vertex not in used:
            print(f'graph component #{N}: ', end='')
            dfs_c(vertex,G,used)
            print('')
            N += 1
    print(f'N = {N}')
    pass


if __name__ == '__main__':
    test0()
    test1()
    test2()
