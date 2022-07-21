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


# процедура подсчета компонент связности
def number_of_connectivity_components(G):
    used = set()
    N = 0
    for vertex in G:
        if vertex not in used:
            print(f'graph component #{N}: ', end='')
            dfs_c(vertex, G, used)
            print('')
            N += 1
    return N


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
    print(f'N comps = {number_of_connectivity_components(G)}')
    print('')

# Алгоритм Косарайю выделения компонент сильной связности
# ориентированного графа.
# Ориентированный граф (орграф) называется сильно связным
# (англ. strongly connected), если любые две его вершины
# s и t сильно связны, то есть если существует ориентированный
# путь из s в t и одновременно ориентированный путь из t в s.


# прямой проход
def dfs_k(vertex, G, used, stack):
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs_k(neighbor, G, used, stack)
    stack.append(vertex)


# обратный проход
def dfs_k_backward(vertex, G, used):
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs_k_backward(neighbor, G, used)


# процедура инвертирования графа
def invert(G: dict):
    H = dict()
    for vertex in G:
        H[vertex] = set()
    for vertex in G:
        for v in G[vertex]:
            H[v].add(vertex)
    return H


# форматированный вывод графа
def printg(G: dict):
    for vertex in G:
        print(f'{vertex}: {G[vertex]}')


# процедура подсчета компонент
# сильной связности орграфа
def n_strongly_comp(G):
    used = set()
    stack = []
    N = 0
    # делаем прямой обход орграфа и заполняем попутно стек
    # считаем компоненты слабой связности
    for vertex in G:
        if vertex not in used:
            print(f'graph weekly connected component #{N}: ', end='')
            dfs_k(vertex, G, used, stack)
            print('')
            N += 1
    print(f'N weekly comps = {N}')
    print(f'stack: {stack}')
    # получаем инвертированный орграф
    H = invert(G)
    print(f'inverted graph:')
    printg(H)
    # обходим инвертированный орграф
    # учитывая порядок вершин в стеке
    # считаем компоненты сильной связности
    N = 0
    used = set()
    print('')
    while stack != []:
        vertex = stack.pop()
        if vertex not in used:
            print(f'strongly comp #{N}: ', end='')
            dfs_k_backward(vertex, H, used)
            print('')
            N += 1
    return N


def test2():
    Graphs = [{'A': {'B'},
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
    for G in Graphs:
        print(f'N strongly comps: {n_strongly_comp(G)}')
        print('')

# Топологическая сортировка. Алгоритм Тарьяна.
# Если орграф не содержит циклов, то его вершины
# можно пронумеровать так, что любое ребро идет
# от вершины с меньшим номером к вершине с большим.
# Сложность по времени алгоритма Тарьяна - О(N),
# где N - число вершин. Вершина - это число от 1
# до N.

# вариант с множеством used


def dfs_t(vertex, G, used, ans):
    used.add(vertex)
    for neighbor in G[vertex]:
        if neighbor not in used:
            dfs_t(neighbor, G, used, ans)
    # добавляем вершину в список на обратном
    # ходу рекурсии
    ans.append(vertex)


def topsort(G):
    used = set()
    # список, в который будет сохраняться топологический порядок вершины
    ans = []
    for vertex in G:
        if vertex not in used:
            dfs_t(vertex, G, used, ans)
    # необходимо инвертировать список
    # так как элементы в него заносились
    # на обратном ходу рекурсии в dfs_t
    ans[:] = ans[::-1]

    return ans


def test3():
    Graphs = [{1: {2},
               2: {3},
               3: {1}},
              {1: {3, 4, 5},
               2: {5},
               3: {6, 7},
               4: {7},
               5: {8},
               6: {9},
               7: {9},
               8: {10, 12},
               9: {10, 13},
               10: {11, 13},
               11: {},
               12: {},
               13: {}},
              {1: {2, 3},
               2: {4},
               3: {4},
               4: {}},
              {0: {},
               1: {},
               2: {3},
               3: {1},
               4: {0, 1},
               5: {0, 2}}]

    for i, G in enumerate(Graphs):
        print(f'graph #{i} has topological order: {topsort(G)}')

# вариант со списком visited


def dfs_t_v(vertex, G, visited, ans):
    visited[vertex] = True
    for neighbor in G[vertex]:
        if not visited[neighbor]:
            dfs_t_v(neighbor, G, visited, ans)
    # добавляем вершину в список на обратном
    # ходу рекурсии
    ans.append(vertex)


def topsort_v(G):
    # число вершин графа
    n = len(G)
    # вершина с индексом 0 фиктивная - ее нет в графе
    visited = [False] * (n+1)
    # список, в который будет сохраняться топологический порядок вершины
    ans = []
    for vertex in range(1, n+1):
        if not visited[vertex]:
            dfs_t_v(vertex, G, visited, ans)
    # необходимо инвертировать список
    # так как элементы в него заносились
    # на обратном ходу рекурсии в dfs_t
    ans[:] = ans[::-1]

    return ans


def test4():
    Graphs = [{1: {2},
               2: {3},
               3: {1}},
              {1: {3, 4, 5},
               2: {5},
               3: {6, 7},
               4: {7},
               5: {8},
               6: {9},
               7: {9},
               8: {10, 12},
               9: {10, 13},
               10: {11, 13},
               11: {},
               12: {},
               13: {}},
              {1: {2, 3},
               2: {4},
               3: {4},
               4: {}},
              {1: {},
               2: {},
               3: {4},
               4: {2},
               5: {1, 2},
               6: {1, 3}}]

    for i, G in enumerate(Graphs):
        print(f'graph #{i} has topological order: {topsort_v(G)}')


# поиск цикла в орграфе
# используем 3 цвета:
# 0 - вершина не посещалась ни разу
# 1 - вершина посещена на прямом ходе рекурсии dfs
# 2 - вершина посещена на обратном ходе рекурсии dfs
# если в ходе рекурсии встретилась смежная вершина цвета 1
# значит найден цикл
def dfs_cycle(vertex, G, colored):
    colored[vertex] = 1
    for neighbor in G[vertex]:
        if colored[neighbor] == 0:
            if dfs_cycle(neighbor, G, colored):
                return True
        elif colored[neighbor] == 1:
            return True
    colored[vertex] = 2
    return False


def find_cycle(G):
    colored = {v: 0 for v in G}
    for vertex in G:
        if dfs_cycle(vertex, G, colored):
            return True
    return False


def test5():
    Graphs = [{1: {2},
               2: {3},
               3: {1}},
              {1: {3, 4, 5},
               2: {5},
               3: {6, 7},
               4: {7},
               5: {8},
               6: {9},
               7: {9},
               8: {10, 12},
               9: {10, 13},
               10: {7, 11, 13},
               11: {},
               12: {},
               13: {}},
              {1: {2, 3},
               2: {4},
               3: {4},
               4: {}},
              {1: {},
               2: {},
               3: {4},
               4: {2},
               5: {1, 2},
               6: {1, 3}}]

    for i, G in enumerate(Graphs):
        print(f'graph #{i} has cycle: {find_cycle(G)}')


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
