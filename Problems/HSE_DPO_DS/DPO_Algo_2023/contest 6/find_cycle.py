# https://contest.yandex.ru/contest/49987/problems/E/
# Дан неориентированный граф. Требуется определить, есть ли в нем цикл, и, если есть, вывести его.
# В первой строке дано одно число n — количество вершин в графе (1 ≤ n ≤ 500). Далее в n строках задан сам граф
# матрицей смежности.
# Если в исходном графе нет цикла, то выведите «NO». Иначе, в первой строке выведите «YES», во второй строке выведите
# число k — количество вершин в цикле, а в третьей строке выведите k различных чисел — номера вершин, которые
# принадлежат циклу в порядке обхода (обход можно начинать с любой вершины цикла). Если циклов несколько, то выведите
# любой.

def find_cycle(adj_m):
    n = len(adj_m[0])
    starting_vertices = set((v for v in range(n)))
    used = [0] * n
    parents = [-1] * n
    while starting_vertices:
        start_vertex = starting_vertices.pop()
        used[start_vertex] = 1
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            for neighbour in range(n):
                if adj_m[vertex][neighbour]:
                    if not used[neighbour]:
                        stack.append(neighbour)
                        used[neighbour] = 1
                        parents[neighbour] = vertex
                        starting_vertices.discard(neighbour)
                    elif parents[vertex] != neighbour:
                        print('YES')
                        start = parents[vertex]
                        cycle = [neighbour + 1, vertex + 1, start + 1]
                        while not adj_m[start][neighbour]:
                            start = parents[start]
                            cycle.append(start + 1)

                        print(len(cycle))
                        print(*cycle)
                        return

    print('NO')


def test0():
    test_data = ([[0, 1, 0, 0, 0],
                  [1, 0, 0, 0, 0],
                  [0, 0, 0, 1, 1],
                  [0, 0, 1, 0, 1],
                  [0, 0, 1, 1, 0]],
                 [[0, 1, 1],
                  [1, 0, 1],
                  [1, 1, 0]],
                 [[0, 0, 1, 0],
                  [0, 0, 0, 1],
                  [1, 0, 0, 0],
                  [0, 1, 0, 0]])
    for adj_m in test_data:
        find_cycle(adj_m)


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
