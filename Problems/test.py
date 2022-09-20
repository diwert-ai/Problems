def color_map(region):
    n, m, graph, vertices = len(region), len(region[0]), dict(), set()
    for line in region:
        vertices = vertices | set(line)
    for vertex in vertices:
        graph[vertex] = set()

    def cell(row, col):
        return region[row][col] if 0 <= row < n and 0 <= col < m else None

    def add_edge(v1, v2):
        if v2 is not None and v1 != v2:
            graph[v1].add(v2)
            graph[v2].add(v1)

    for i in range(n):
        for j in range(m):
            vertex, right_neighbor, bottom_neighbor = region[i][j], cell(i, j + 1), cell(i + 1, j)
            add_edge(vertex, right_neighbor)
            add_edge(vertex, bottom_neighbor)

    ordered_vertices = sorted(vertices, key=lambda x: -len(graph[x]))
    print(graph)
    print(ordered_vertices)
    return [1, 1]


def test0():
    v_s = set()
    r = ((1, 2, 3, 1, 1, 1, 1, 1, 1),
         (0, 2, 2, 2, 2, 2, 2, 1, 4))

    for rw in r:
        v_s = v_s | set(rw)

    print(v_s)


def test1():
    color_map(((0, 0, 0, 1, 4, 4, 4, 4, 4),
               (0, 1, 1, 1, 3, 3, 3, 3, 4),
               (0, 1, 1, 3, 3, 6, 5, 3, 4),
               (1, 1, 1, 3, 2, 6, 5, 5, 9),
               (1, 1, 1, 2, 2, 6, 6, 6, 9),
               (7, 8, 9, 9, 9, 9, 9, 9, 9),
               (7, 8, 8, 8, 8, 8, 8, 8, 8),
               (7, 7, 7, 7, 7, 7, 7, 7, 7)))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
