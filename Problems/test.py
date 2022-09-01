def add_edge(v1, v2, g):
    if v1 not in g:
        g[v1] = set()
    if v2 not in g:
        g[v2] = set()
    g[v1].add(v2)


def dfs_t(vertex, graph, used, ans):
    used.add(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in used:
            dfs_t(neighbor, graph, used, ans)
    # добавляем вершину в список на обратном
    # ходу рекурсии
    ans.append(vertex)


def topsort(graph):
    used = set()
    # список, в который будет сохраняться топологический порядок вершины
    ans = []
    for vertex in graph:
        if vertex not in used:
            dfs_t(vertex, graph, used, ans)
    # необходимо инвертировать список
    # так как элементы в него заносились
    # на обратном ходу рекурсии в dfs_t
    ans[:] = ans[::-1]

    return ans


def recover_secret(triplets):
    graph = dict()
    for triplet in triplets:
        for i in range(2):
            v1 = triplet[i]
            v2 = triplet[i+1]
            add_edge(v1, v2, graph)
    return ''.join(topsort(graph))


def test0():
    # noinspection SpellCheckingInspection
    secret = "whatisup"
    triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]
    print(recover_secret(triplets) == secret)


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
