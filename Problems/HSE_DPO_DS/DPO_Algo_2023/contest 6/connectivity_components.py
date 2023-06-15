# https://contest.yandex.ru/contest/49987/problems/F/
# Дан неориентированный невзвешенный граф. Необходимо посчитать количество его компонент связности и вывести их.
# Во входном файле записано два числа N и M (0 < N ≤ 100000, 0 ≤ M ≤ 100000). В следующих M строках записаны по два
# числа i и j (1 ≤ i, j ≤ N), которые означают, что вершины i и j соединены ребром.
# В первой строчке выходного файла выведите количество компонент связности. Далее выведите сами компоненты связности в
# следующем формате: в первой строке количество вершин в компоненте, во второй - сами вершины в произвольном порядке.

def show_conn_comps(n, edges):
    graph = {i: set() for i in range(n)}

    for v1, v2 in edges:
        graph[v1 - 1].add(v2 - 1)
        graph[v2 - 1].add(v1 - 1)

    components = []
    comp_index = 0
    starting_vertices = set((v for v in range(n)))
    used = [0] * n

    while starting_vertices:
        start_vertex = starting_vertices.pop()
        used[start_vertex] = 1
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            components.append([])
            components[comp_index].append(vertex)
            for neighbour in graph[vertex]:
                if not used[neighbour]:
                    stack.append(neighbour)
                    used[neighbour] = 1
                    starting_vertices.discard(neighbour)
        comp_index += 1

    print(comp_index)
    for i in range(comp_index):
        print(len(components[i]))
        print(*(i + 1 for i in components[i]))


def test0():
    test_data = ((6, [(3, 1), (1, 2), (5, 4), (2, 3)]),
                 (6, [(4, 2), (1, 4), (6, 4), (3, 6)]))

    for n, edges in test_data:
        show_conn_comps(n, edges)
        print('-------------')


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
