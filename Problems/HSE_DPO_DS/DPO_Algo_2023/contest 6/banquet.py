# https://contest.yandex.ru/contest/49987/problems/D/
# На банкет были приглашены N Очень Важных Персон (ОВП). Были поставлены 2 стола. Столы достаточно большие, чтобы все
# посетители банкета могли сесть за любой из них. Проблема заключается в том, что некоторые ОВП не ладят друг с другом
# и не могут сидеть за одним столом. Вас попросили определить, возможно ли всех ОВП рассадить за двумя столами.

# В первой строке входных данных содержатся два числа: N и M (1 <= N,M <= 100), где N – количество ОВП, а M – количество
# пар ОВП, которые не могут сидеть за одним столом. В следующих M строках записано по 2 числа – пары ОВП, которые не
# могут сидеть за одним столом.

# Если способ рассадить ОВП существует, то выведите YES в первой строке и номера ОВП, которых необходимо посадить за
# первый стол, во второй строке. В противном случае в первой и единственной строке выведите NO.

def answer(pairs, n):
    graph = {i: set() for i in range(n)}

    for v1, v2 in pairs:
        graph[v1 - 1].add(v2 - 1)
        graph[v2 - 1].add(v1 - 1)

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
            for neighbour in graph[vertex]:
                if not used[neighbour]:
                    stack.append(neighbour)
                    used[neighbour] = color
                    starting_vertices.discard(neighbour)
                elif used[neighbour] != color:
                    print('NO')
                    return

    print('YES')
    print(*(i + 1 for i in range(n) if used[i] == 1))


def test0():
    test_data = ((4,  [(1, 2), (2, 3), (1, 3)]),
                 (4,  [(1, 2), (3, 4)]))

    for n, pairs in test_data:
        answer(pairs, n)


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
