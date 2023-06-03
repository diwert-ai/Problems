# https://contest.yandex.ru/contest/49890/problems/F/
# Дан неориентированный невзвешенный граф. Для него вам необходимо найти количество вершин, лежащих в одной компоненте
# связности с данной вершиной (считая эту вершину).

# В первой строке входных данных содержатся два числа: N и S (1 ≤ N ≤ 100; 1 ≤ S ≤ N), где N – количество вершин графа,
# а S – заданная вершина. В следующих N строках записано по N чисел – матрица смежности графа, в которой 0 означает
# отсутствие ребра между вершинами, а 1 – его наличие. Гарантируется, что на главной диагонали матрицы всегда стоят
# нули.

def connectivity_component_size(adj_m, start_vertex):
    v = len(adj_m[0])
    graph = {x: set() for x in range(v)}

    for v1 in range(v):
        for v2, val in enumerate(adj_m[v1]):
            if v2 > v1 and val:
                graph[v1].add(v2)
                graph[v2].add(v1)

    stack, used = [start_vertex - 1], [start_vertex - 1]

    while stack:
        vertex = stack.pop()
        for neighbour in graph[vertex]:
            if neighbour not in used:
                used.append(neighbour)
                stack.append(neighbour)

    return len(used)


def test0():
    test_data = (([[0, 1, 1], [1, 0, 0], [1, 0, 0]], 1),
                 ([[0, 1, 1, 1], [1, 0, 1, 0], [1, 1, 0, 1], [1, 0, 1, 0]], 4),
                 ([[0, 1, 0, 1], [1, 0, 0, 0], [0, 0, 0, 0], [1, 0, 0, 0]], 3)
                 )
    for adj_m, start in test_data:
        print(connectivity_component_size(adj_m, start))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
