# https://contest.yandex.ru/contest/49987/problems/A/
# Алгоритм Дейкстры
#
# Дан ориентированный взвешенный граф. Для него вам необходимо найти кратчайшее расстояние от вершины S до вершины F.
# В первой строке входных данных содержатся три числа: N, S и F (1 ≤ N ≤ 100, 1 ≤ S, F ≤ N), где N – количество вершин
# графа. В следующих N строках записаны по N чисел – матрица смежности графа, где число в i-ой строке и j-ом столбце
# соответствует ребру из i в j: -1 означает отсутствие ребра между вершинами, а любое неотрицательное число – наличие
# ребра данного веса. На главной диагонали матрицы всегда записаны нули.

def min_distance(start, finish, adj_m):
    start -= 1
    finish -= 1
    n = len(adj_m[0])
    used, dists = [0] * n, [float('inf')] * n
    dists[start] = 0

    while start != finish:
        used[start] = 1
        for i in range(n):
            edge_weight = adj_m[start][i]
            if edge_weight > 0:
                dists[i] = min(dists[i], dists[start] + edge_weight)

        min_dist = float('inf')

        for i in range(n):
            if not used[i] and min_dist > dists[i]:
                min_dist = dists[i]
                start = i

        if min_dist == float('inf'):
            return -1

    return dists[finish]


def test0():
    test_data = ((2, 1, [[0, 1, 1], [4, 0, 1], [2, 1, 0]]), )
    for start, finish, adj_m in test_data:
        print(min_distance(start, finish, adj_m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
