# https://contest.yandex.ru/contest/50346/problems/B/
# Дан неориентированный граф. Над ним в заданном порядке производят операции следующих двух типов:
# ∙ cut — разрезать граф, то есть удалить из него ребро;
# ∙ ask — проверить, лежат ли две вершины графа в одной компоненте связности.
# Известно, что после выполнения всех операций типа cut рёбер в графе не осталось. Найдите результат выполнения каждой
# из операций типа ask.

def process_queries(queries):
    n = len(queries)
    parents = [i for i in range(n)]

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

    result = []
    while queries:
        query, v1, v2 = queries.pop()
        root_v1, root_v2 = find(v1), find(v2)
        if query == 'ask':
            result.append('YES' if root_v1 == root_v2 else 'NO')
        else:
            parents[root_v2] = root_v1

    return result[::-1]


def test0():
    test_data = ([('ask', 3, 3), ('cut', 1, 2), ('ask', 1, 2), ('cut', 1, 3),
                  ('ask', 2, 1), ('cut', 2, 3), ('ask', 3, 1)],)
    for queries in test_data:
        print(*process_queries(queries))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
