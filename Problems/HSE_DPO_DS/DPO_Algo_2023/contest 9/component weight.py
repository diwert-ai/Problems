# https://contest.yandex.ru/contest/50346/problems/D/
# В неориентированный взвешенный граф добавляют ребра. Напишите программу, которая в некоторые моменты находит сумму
# весов ребер в компоненте связности.

def process_queries(queries, n):
    parents = [i for i in range(n)]
    size = [0 for _ in range(n)]

    def find(a):
        root = a
        while parents[root] != root:
            root = parents[root]

        # делаем сжатие путей
        while parents[a] != a:
            next_element = parents[a]
            parents[a] = root
            a = next_element

        return root

    for query in queries:
        if query[0] == 1:
            v1, v2, w = query[1:]
            root_v1, root_v2 = find(v1 - 1), find(v2 - 1)
            parents[root_v2] = root_v1
            size[root_v1] += w
        else:
            print(size[find(query[1] - 1)])


def test0():
    test_data = (([(2, 1), (1, 1, 2, 1), (2, 1), (1, 2, 4, 2), (2, 1),
                  (1, 1, 4, 3), (2, 1), (1, 3, 5, 3), (2, 5), (2, 6)], 6), )
    for queries, n in test_data:
        process_queries(queries, n)


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
