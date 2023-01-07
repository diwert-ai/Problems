# https://py.checkio.org/ru/mission/disposable-teleports/
# На острове есть сеть станций, которые соединены сетью телепортов.
# Однако, у этих устройств есть проблема - очень долгая перезарядка.
# И по сути вы можете использовать каждый телепорт только один раз,
# после он выключается и не работает. Но вы можете посещать любую
# станцию сколько угодно раз, если нужно.
#
# Вы начинаете на станции номер 1 и должны попытаться посетить все станции
# хотя бы по разу и вернутся на изначальную точку. Карта телепортов представлена
# как строка в которой через запятую перечислены телепорты. Каждый телепорт
# описывается двумя цифрами, обозначающими станции, которые он соединяет.
# Например "12" или "32". Порядок не важен. Вам необходимо найти маршрут,
# который проходит через все станции. Он должен быть представлен, как строка
# в которой перечислены номера станций, в порядке, как они должны быть посещены.


# Идея решения: редуцируем граф так, чтобы он стал эйлеровым (убираем ребра так, чтобы
# все вершины имели четную степень), затем находим эйлеров цикл.
def add_edge(graph, edge):
    v1 = edge.pop()
    v2 = edge.pop()
    graph[v1].add(v2) if v1 in graph else graph.update({v1: {v2}})
    graph[v2].add(v1) if v2 in graph else graph.update({v2: {v1}})


def add_edges(graph, edges):
    for edge in edges:
        add_edge(graph, edge)


def remove_edge(graph, edge):
    v, w = edge
    graph[w].remove(v)
    graph[v].remove(w)


def reduce_graph(graph):
    do_reduce = True
    while do_reduce:
        do_reduce = False
        for v in graph:
            if len(graph[v]) % 2:
                do_reduce = True
                break
        if do_reduce:
            do_find_max = True
            for w in graph[v]:
                if len(graph[w]) % 2:
                    remove_edge(graph, (v, w))
                    do_find_max = False
                    break
            if do_find_max:
                w = max(graph[v], key=lambda x: len(graph[x]))
                remove_edge(graph, (v, w))


def to_edges(graph):
    result = []
    for v in graph:
        for w in graph[v]:
            if v + w not in result and w + v not in result:
                result.append(v + w)

    return list(map(set, result))


def checkio(teleports_string):
    result, edges, graph = list(), list(map(set, teleports_string.split(','))), dict()
    add_edges(graph, edges)
    reduce_graph(graph)
    edges = to_edges(graph)

    def find_euler_path(vertex):
        for edge in edges.copy():
            if vertex in edge:
                edges.remove(edge)
                edge.remove(vertex)
                find_euler_path(edge.pop())
        result.append(vertex)

    find_euler_path('1')
    return ''.join(result)


def test0():
    test_strs = ["12,23,34,45,56,67,78,81",
                 "12,28,87,71,13,14,34,35,45,46,63,65",
                 "12,15,16,23,24,28,83,85,86,87,71,74,56",
                 "12,15,16,23,24,28,83,85,86,71,74",
                 "13,14,23,25,34,35,47,56,58,76,68",
                 "13,14,23,25,34,35,47,56,58,76,68",
                 "12,17,87,86,85,82,65,43,35,46"]
    for test_str in test_strs:
        print(checkio(test_str))


def test1():
    test_str = "13,14,23,25,34,35,47,56,58,76,68"
    graph = dict()
    add_edges(graph, list(map(set, test_str.split(','))))
    print(to_edges(graph))
    reduce_graph(graph)
    print(to_edges(graph))


def test2():
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if teleport not in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"
    print('All asserts have passed!')


if __name__ == '__main__':
    test_funcs = [test0, test1, test2]
    for test in test_funcs:
        test()
