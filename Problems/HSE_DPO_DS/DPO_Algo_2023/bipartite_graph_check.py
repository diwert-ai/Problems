# Проверка орграфа на двудольность. Орграф задан матрицей смежности.

def is_bipartite(adj_m):
    n = len(adj_m)

    # Раскраска в два цвета с помощью DFS работает именно на неориентированном графе,
    # при этом двудольность не зависит от ориентации ребер, поэтому предварительно
    # симметризуем матрицу смежности

    for i in range(n):
        for j in range(n):
            if adj_m[i][j] == 1:
                adj_m[j][i] = 1

    starting_vertices = set((v for v in range(n)))
    used = [0] * n
    while starting_vertices:
        start_vertex = starting_vertices.pop()
        color = 1
        used[start_vertex] = color
        stack = [start_vertex]
        while stack:
            vertex = stack.pop()
            color = 3 - used[vertex]
            for neighbour in range(n):
                if adj_m[vertex][neighbour]:
                    if not used[neighbour]:
                        stack.append(neighbour)
                        used[neighbour] = color
                        starting_vertices.discard(neighbour)
                    elif used[neighbour] != color:
                        print(used)
                        return False

    return True


def test0():
    test_data = ([[0, 1, 0, 0, 0, 0],
                  [0, 0, 0, 0, 0, 0],
                  [0, 0, 0, 1, 0, 0],
                  [1, 0, 0, 0, 0, 0],
                  [1, 0, 0, 0, 0, 1],
                  [0, 0, 0, 1, 0, 0]], )
    for adj_m in test_data:
        print(is_bipartite(adj_m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
