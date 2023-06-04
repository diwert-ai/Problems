# https://contest.yandex.ru/contest/49987/problems/B/
# Дейкстра: восстановление пути.
#
# Дан ориентированный взвешенный граф. Найдите кратчайший путь от одной заданной вершины до другой.
#
# В первой строке входных данных содержатся три числа: N, S и F (1 ≤ N ≤ 100, 1 ≤ S, F ≤ N), где N – количество вершин
# графа, S – начальная вершина, а F – конечная. В следующих N строках вводится по N чисел, не превосходящих 100, –
# матрица смежности графа, где −1 означает отсутствие ребра между вершинами, а любое неотрицательное число – присутствие
# ребра данного веса. На главной диагонали матрицы записаны нули.

def get_shortest_path(start, finish, adj_m):
    finish -= 1
    start -= 1
    n, first_start = len(adj_m[0]), start
    used, dists, path, result = [0] * n, [float('inf')] * n, [-1] * n, list()
    dists = [float('inf')] * n
    dists[start] = 0

    while start != finish:
        used[start] = 1
        for i in range(n):
            edge_weight = adj_m[start][i]
            if edge_weight > 0 and dists[start] + edge_weight < dists[i]:
                dists[i] = dists[start] + edge_weight
                path[i] = start

        min_dist = float('inf')

        for i in range(n):
            if not used[i] and min_dist > dists[i]:
                min_dist = dists[i]
                start = i

        if min_dist == float('inf'):
            return (-1, )

    while finish != first_start:
        result.append(finish + 1)
        finish = path[finish]

    result.append(first_start + 1)

    return result[::-1]


def test0():
    test_data = ((2, 1, [[0, 1, 1], [4, 0, 1], [2, 1, 0]]), )
    for start, finish, adj_m in test_data:
        print(*get_shortest_path(start, finish, adj_m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
