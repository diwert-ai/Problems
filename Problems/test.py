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

    def dfs(vert, clr):
        used.add(vert)
        if not colored_vertices[vert] and all((colored_vertices[neighbor] != clr for neighbor in graph[vert])):
            colored_vertices[vert] = clr
        for neighbor in graph[vert]:
            if neighbor not in used:
                dfs(neighbor, clr)

    ordered_vertices = sorted(vertices, key=lambda x: -len(graph[x]))
    colored_vertices = {vertex: None for vertex in vertices}
    print(f'graph: {graph}')
    print(f'o vertices: {ordered_vertices}')
    for color in range(1, 5):
        used = set()
        for vertex in ordered_vertices[::-1]:
            if not colored_vertices[vertex]:
                dfs(vertex, color)

    return [colored_vertices[vertex] for vertex in vertices]


def test0():
    v_s = set()
    r = ((1, 2, 3, 1, 1, 1, 1, 1, 1),
         (0, 2, 2, 2, 2, 2, 2, 1, 4))

    for rw in r:
        v_s = v_s | set(rw)

    print(v_s)


def test1():
    print(color_map(((0, 0, 0, 1, 4, 4, 4, 4, 4),
                     (0, 1, 1, 1, 3, 3, 3, 3, 4),
                     (0, 1, 1, 3, 3, 6, 5, 3, 4),
                     (1, 1, 1, 3, 2, 6, 5, 5, 9),
                     (1, 1, 1, 2, 2, 6, 6, 6, 9),
                     (7, 8, 9, 9, 9, 9, 9, 9, 9),
                     (7, 8, 8, 8, 8, 8, 8, 8, 8),
                     (7, 7, 7, 7, 7, 7, 7, 7, 7))))

    print(color_map(((13, 13, 13, 13, 13, 13, 14, 14, 14, 14,),
                     (13, 0, 0, 1, 1, 2, 2, 3, 3, 14,),
                     (13, 4, 5, 5, 6, 6, 7, 7, 8, 14,),
                     (13, 9, 9, 10, 10, 11, 11, 12, 12, 14,),
                     (13, 13, 13, 13, 14, 14, 14, 14, 14, 14,),)))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
