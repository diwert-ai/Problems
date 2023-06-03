# https://contest.yandex.ru/contest/49890/problems/D/
# Напомним, что ориентированный граф называется транзитивным, если для любых трех различных вершин u, v и w из того,
# что из u в вершину v ведет ребро и из вершины v в вершину w ведет ребро, следует, что из вершины u в вершину w ведет
# ребро. Проверьте, что заданный ориентированный граф является транзитивным.

# Сначала вводится число n (1<=n<=100) – количество вершин в графе, а затем n строк по n чисел, каждое из которых равно
# 0 или 1, – его матрица смежности.


def is_transitive(adjacency_matrix):
    v = len(adjacency_matrix[0])

    for i in range(v):
        for j in range(v):
            for k in range(v):
                if adjacency_matrix[i][j] and adjacency_matrix[j][k] and not adjacency_matrix[i][k]:
                    return 'NO'
    return 'YES'


def test0():
    test_data = ([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]],
                 [[0, 0, 1], [0, 0, 1], [1, 1, 0]],
                 [[0, 1, 1, 1], [0, 0, 1, 0], [0, 0, 0, 0], [0, 0, 1, 0]]
                 )

    for adj_m in test_data:
        print(is_transitive(adj_m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
