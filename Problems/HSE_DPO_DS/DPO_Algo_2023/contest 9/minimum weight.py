# https://contest.yandex.ru/contest/50346/problems/E/
# От вас требуется определить вес минимального остовного дерева для неориентированного взвешенного связного графа.

def calc_minimum_weight(edges):
    n = len(edges)
    edges.sort(key=lambda x: x[2])
    parents = [i for i in range(n)]

    def find(v):
        root = v
        while parents[root] != root:
            root = parents[root]

        # делаем сжатие путей
        while parents[v] != v:
            next_element = parents[v]
            parents[v] = root
            v = next_element

        return root

    result = 0
    for v1, v2, w in edges:
        root_v1, root_v2 = find(v1-1), find(v2-1)
        if root_v1 != root_v2:
            result += w
            parents[root_v1] = root_v2

    return result


def test0():
    test_data = ([(1, 2, 1), (2, 3, 2), (3, 1, 3)], )
    for edges in test_data:
        print(calc_minimum_weight(edges))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
