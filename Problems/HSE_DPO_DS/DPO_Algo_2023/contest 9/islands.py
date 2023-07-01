# https://contest.yandex.ru/contest/50346/problems/C/
# Одно разбросанное на островах Океании государство решило создать сеть автомобильных дорог (вернее, мостов). По каждому
# мосту можно перемещаться в обе стороны. Был разработан план очередности строительства мостов и известно, что после
# постройки всех мостов можно будет проехать по ним с каждого острова на каждый (возможно, через некоторые промежуточные
# острова).
#
# Однако, этот момент может наступить до того, как будут построены все мосты. Ваша задача состоит в нахождении такого
# минимального количества мостов, после постройки которого (в порядке строительства по плану) можно будет попасть с
# любого острова на любой другой.

def process_bridges(bridges, n):
    parents = [i for i in range(n)]
    size = [1 for _ in range(n)]

    def find(a):
        root = a
        while parents[root] != root:
            root = parents[root]

        # таки делаем сжатие путей
        while parents[a] != a:
            next_element = parents[a]
            parents[a] = root
            a = next_element

        return root

    for i, (i1, i2) in enumerate(bridges, 1):
        root_i1, root_i2 = find(i1), find(i2)
        if root_i1 != root_i2:
            # делаем ранговую эвристику
            if size[root_i1] > size[root_i2]:
                root_i1, root_i2 = root_i1, root_i2
            parents[root_i1] = root_i2  # union(a, b)
            size[root_i2] += size[root_i1]
            n -= 1

        if n == 1:
            return i

    return -1


def test0():
    test_data = (([(0, 1), (0, 2), (1, 2), (2, 3), (3, 0)], 4), )
    for bridges, n in test_data:
        print(process_bridges(bridges, n))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
