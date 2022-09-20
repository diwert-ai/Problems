# обход графа в глубину Depth-First Search, DFS
# из лекции Хирьянова:
# https://www.youtube.com/watch?v=sBJ7ana1fgI&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=23

# Позволяет:
# 1. выделить компоненту связности;
# 2. подсчитать кол-во компонент;
# 3. найти простой цикл (хотя бы один, если существует);
# 4. определить граф двудольный или нет (можно ли раскрасить
# вершины графа в 2 цвета так, что любое ребро соединяет
# только разноцветные вершины)
# 5. найти мосты и точки сочленения
# 6. с орграфами: выделение компонент сильной связности -
# делается 2 обхода в глубину - алгоритм Косарайю
# 7. топологическая сортировка


def dfs(vertex, g, used=None):
    used = used or set()
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in g[vertex]:
        if neighbor not in used:
            dfs(neighbor, g, used)


def test0():
    g = {0: {18, 1, 14},
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
    dfs(0, g)
    print('')


# видоизмененная функция обхода для подсчета компонент связности
def dfs_c(vertex, g, used):
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in g[vertex]:
        if neighbor not in used:
            dfs_c(neighbor, g, used)


# процедура подсчета компонент связности
def number_of_connectivity_components(g):
    used = set()
    n = 0
    for vertex in g:
        if vertex not in used:
            print(f'graph component #{n}: ', end='')
            dfs_c(vertex, g, used)
            print('')
            n += 1
    return n


def test1():
    g = {0: {18, 1, 14},
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
    print(f'n comps = {number_of_connectivity_components(g)}')
    print('')

# Алгоритм Косарайю выделения компонент сильной связности
# ориентированного графа.
# Ориентированный граф (орграф) называется сильно связным
# (англ. strongly connected), если любые две его вершины
# s и t сильно связны, то есть если существует ориентированный
# путь из s в t и одновременно ориентированный путь из t в s.


# прямой проход
def dfs_k(vertex, g, used, stack):
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in g[vertex]:
        if neighbor not in used:
            dfs_k(neighbor, g, used, stack)
    stack.append(vertex)


# обратный проход
def dfs_k_backward(vertex, g, used):
    print(vertex, end=' ')
    used.add(vertex)
    for neighbor in g[vertex]:
        if neighbor not in used:
            dfs_k_backward(neighbor, g, used)


# процедура инвертирования графа
def invert(g: dict):
    h = dict()
    for vertex in g:
        h[vertex] = set()
    for vertex in g:
        for v in g[vertex]:
            h[v].add(vertex)
    return h


# форматированный вывод графа
def print_graph(g: dict):
    for vertex in g:
        print(f'{vertex}: {g[vertex]}')


# процедура подсчета компонент
# сильной связности орграфа
def n_strongly_comp(g):
    used = set()
    stack = []
    n = 0
    # делаем прямой обход орграфа и заполняем попутно стек
    # считаем компоненты слабой связности
    for vertex in g:
        if vertex not in used:
            print(f'graph weekly connected component #{n}: ', end='')
            dfs_k(vertex, g, used, stack)
            print('')
            n += 1
    print(f'n weekly comps = {n}')
    print(f'stack: {stack}')
    # получаем инвертированный орграф
    h = invert(g)
    print(f'inverted graph:')
    print_graph(h)
    # обходим инвертированный орграф
    # учитывая порядок вершин в стеке
    # считаем компоненты сильной связности
    n = 0
    used = set()
    print('')
    while stack:
        vertex = stack.pop()
        if vertex not in used:
            print(f'strongly comp #{n}: ', end='')
            dfs_k_backward(vertex, h, used)
            print('')
            n += 1
    return n


def test2():
    graphs = [{'A': {'B'},
               'B': {'C', 'D'},
               'C': {'A'},
               'D': {'E'},
               'F': {'D'},
               'E': {'F'},
               'g': {'F', 'h'},
               'h': {'I'},
               'I': {'J'},
               'J': {'g'},
               'K': {'J'}},
              {'A': {'B'},
               'B': {'C', 'D'},
               'C': {'E'},
               'D': {},
               'E': {'D', 'F'},
               'F': {'g'},
               'g': {'E', 'h'},
               'h': {}},
              {'A': {'B', 'D'},
               'B': {'C', 'E'},
               'C': {'A', 'D'},
               'D': {'E', 'K'},
               'E': {'C', 'h'},
               'F': {'E', 'h', 'J'},
               'g': {'F', 'J'},
               'h': {'g'},
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
    for g in graphs:
        print(f'n strongly comps: {n_strongly_comp(g)}')
        print('')

# Топологическая сортировка. Алгоритм Тарьяна.
# Если орграф не содержит циклов, то его вершины
# можно пронумеровать так, что любое ребро идет
# от вершины с меньшим номером к вершине с большим.
# Сложность по времени алгоритма Тарьяна - О(n),
# где n - число вершин. Вершина - это число от 1
# до n.

# вариант с множеством used


def dfs_t(vertex, g, used, ans):
    used.add(vertex)
    for neighbor in g[vertex]:
        if neighbor not in used:
            dfs_t(neighbor, g, used, ans)
    # добавляем вершину в список на обратном
    # ходу рекурсии
    ans.append(vertex)


def topsort(g):
    used = set()
    # список, в который будет сохраняться топологический порядок вершины
    ans = []
    for vertex in g:
        if vertex not in used:
            dfs_t(vertex, g, used, ans)
    # необходимо инвертировать список
    # так как элементы в него заносились
    # на обратном ходу рекурсии в dfs_t
    ans[:] = ans[::-1]

    return ans


def test3():
    graphs = [{1: {2},
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

    for i, g in enumerate(graphs):
        print(f'graph #{i} has topological order: {topsort(g)}')

# вариант со списком visited


def dfs_t_v(vertex, g, visited, ans):
    visited[vertex] = True
    for neighbor in g[vertex]:
        if not visited[neighbor]:
            dfs_t_v(neighbor, g, visited, ans)
    # добавляем вершину в список на обратном
    # ходу рекурсии
    ans.append(vertex)


def topsort_v(g):
    # число вершин графа
    n = len(g)
    # вершина с индексом 0 фиктивная - ее нет в графе
    visited = [False] * (n+1)
    # список, в который будет сохраняться топологический порядок вершины
    ans = []
    for vertex in range(1, n+1):
        if not visited[vertex]:
            dfs_t_v(vertex, g, visited, ans)
    # необходимо инвертировать список
    # так как элементы в него заносились
    # на обратном ходу рекурсии в dfs_t
    ans[:] = ans[::-1]

    return ans


def test4():
    graphs = [{1: {2},
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

    for i, g in enumerate(graphs):
        print(f'graph #{i} has topological order: {topsort_v(g)}')


# поиск цикла в орграфе
# используем 3 цвета:
# 0 - вершина не посещалась ни разу
# 1 - вершина посещена на прямом ходе рекурсии dfs
# 2 - вершина посещена на обратном ходе рекурсии dfs
# если в ходе рекурсии встретилась смежная вершина цвета 1
# значит найден цикл
def dfs_cycle(vertex, g, colored):
    colored[vertex] = 1
    for neighbor in g[vertex]:
        if colored[neighbor] == 0:
            if dfs_cycle(neighbor, g, colored):
                return True
        elif colored[neighbor] == 1:
            return True
    colored[vertex] = 2
    return False


def find_cycle(g):
    colored = {v: 0 for v in g}
    for vertex in g:
        if dfs_cycle(vertex, g, colored):
            return True
    return False


def test5():
    graphs = [{1: {2},
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

    for i, g in enumerate(graphs):
        print(f'graph #{i} has cycle: {find_cycle(g)}')


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
