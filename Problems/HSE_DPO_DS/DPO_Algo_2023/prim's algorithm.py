# Алгоритм Прима (поиск остовного дерева минимальной стоимости в связном неориентированном взвешенном графе)
import heapq as hp


# (graph - это список списков.)
# (i-й список - это список кортежей (w, v), где w - это вес ребра из вершины i в вершину v.)


def prim_mst(graph):
    n = len(graph)
    mst = []
    used = [0] * n
    weights_heap = [(0, 0, 0)]  # куча ребер (вес, стартовая_вершина, конечная вершина).
    # (первый элемент в куче - (0, 0, 0) - фиктивное начало - ребро из нулевой вершины в себя с нулевым весом)
    while len(mst) < n:
        min_weight, from_vertex, to_vertex = hp.heappop(weights_heap)
        if not used[to_vertex]:
            used[to_vertex] = 1
            mst.append((min_weight, from_vertex, to_vertex))
            for weight, vertex in graph[to_vertex]:
                if not used[vertex]:
                    hp.heappush(weights_heap, (weight, to_vertex, vertex))

    return mst


def test0():
    test_graphs = ([[(1, 2), (2, 1)],
                    [(2, 0), (3, 2), (1, 4)],
                    [(1, 0), (3, 1), (4, 3)],
                    [(4, 2), (1, 4), (0, 5)],
                    [(1, 3), (1, 1), (1, 5)],
                    [(1, 4), (0, 3)]],

                   [[(5, 3), (7, 1)],
                    [(7, 0), (8, 2), (7, 4), (9, 3)],
                    [(8, 1), (5, 4)],
                    [(5, 0), (9, 1), (6, 5), (15, 4)],
                    [(5, 2), (7, 1), (15, 3), (8, 5), (9, 6)],
                    [(6, 3), (8, 4), (11, 6)],
                    [(11, 5), (9, 4)]],
                   )

    for graph in test_graphs:
        mst = prim_mst(graph)
        print(mst)
        print('min weight: ', sum([item[0] for item in mst]))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
