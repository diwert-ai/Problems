# https://py.checkio.org/ru/mission/color-map/
# my solution
# not sure if it's the right solution

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

    colored_vertices = {vertex: None for vertex in vertices}
    for color in range(1, 5):
        used = set()
        for vertex in vertices:
            if not colored_vertices[vertex]:
                dfs(vertex, color)

    return list(colored_vertices.values())


def color_graph(g):
    def dfs(vert, clr):
        used.add(vert)
        if not colored_vertices[vert] and all((colored_vertices[neighbor] != clr for neighbor in g[vert])):
            colored_vertices[vert] = clr
        for neighbor in g[vert]:
            if neighbor not in used:
                dfs(neighbor, clr)

    colored_vertices = {vertex: None for vertex in g}
    for color in range(1, 5):
        used = set()
        for vertex in g:
            if not colored_vertices[vertex]:
                dfs(vertex, color)

    return list(colored_vertices.values())


# best clear solution
# https://py.checkio.org/mission/color-map/publications/DiZ/python-3/borders/?ordering=most_voted&filtering=all
def color_map_bc(colored_map):
    # Construct all regions
    regions = {}
    for i, line in enumerate(colored_map):
        for j, cell in enumerate(line):
            regions.setdefault(cell, set()).add(i + 1j * j)

    # Get neighbours for all regions
    neighbours = {}
    for region, cells in regions.items():
        border = set.union(*({c + 1j ** k for k in range(4)} for c in cells)) - cells
        neighbours[region] = {r for r, c in regions.items() if border & c}

    # Color each region with first available color
    c, colors = 0, [0] * len(regions)
    while c < len(regions):
        variants = set(range(colors[c] + 1, 5)) - {colors[n] for n in neighbours[c]}
        colors[c] = len(variants) and min(variants)
        c += 2 * bool(variants) - 1
    return colors


def test0():
    v_s = set()
    r = ((5, 2, 3, 1, 1, 1, 1, 1, 1),
         (0, 2, 2, 2, 2, 2, 2, 1, 4),
         (0, 2, 2, 2, 4, 4, 4, 4, 4),
         (0, 6, 6, 7, 8, 8, 8, 8, 8),
         (0, 7, 7, 7, 7, 8, 8, 8, 8))

    for rw in r:
        v_s = v_s | set(rw)

    print(v_s)
    print(color_map(r))


def test1():
    print(color_map(((0, 0, 0, 1, 4, 4, 4, 4, 4),
                     (0, 1, 1, 1, 3, 3, 3, 3, 4),
                     (0, 1, 1, 3, 3, 6, 5, 3, 4),
                     (1, 1, 1, 3, 2, 6, 5, 5, 9),
                     (1, 1, 1, 2, 2, 6, 6, 6, 9),
                     (7, 8, 9, 9, 9, 9, 9, 9, 9),
                     (7, 8, 8, 8, 8, 8, 8, 8, 8),
                     (7, 7, 7, 7, 7, 7, 7, 7, 7))))

    regions = ((13, 13, 13, 13, 13, 13, 14, 14, 14, 14,),
               (13, 0, 0, 1, 1, 2, 2, 3, 3, 14,),
               (13, 4, 5, 5, 6, 6, 7, 7, 8, 14,),
               (13, 9, 9, 10, 10, 11, 11, 12, 12, 14,),
               (13, 13, 13, 13, 14, 14, 14, 14, 14, 14,),)
    print(color_map(regions))
    print('bc:', color_map_bc(regions))


def test3():
    g = {1: {2, 4, 5, 3, 13},
         2: {1, 4, 7, 3},
         3: {2, 7, 8, 11, 1},
         4: {1, 2, 5, 6, 7},
         5: {1, 4, 6, 12, 13, 11},
         6: {5, 4, 7, 10, 12, 2},
         7: {2, 3, 8, 10, 6, 4, 9},
         8: {3, 9, 7, 11},
         9: {8, 10, 11, 7},
         10: {7, 9, 11, 12, 6},
         11: {13, 12, 10, 9, 3, 5, 8},
         12: {6, 5, 10, 11, 13},
         13: {11, 12, 5, 1}}
    print('t3: ', color_graph(g))


if __name__ == '__main__':
    test_funcs = [test0, test1, test3]
    for test in test_funcs:
        test()
