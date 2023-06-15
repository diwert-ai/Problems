# https://contest.yandex.ru/contest/49987/problems/G/
# Во время контрольной работы профессор Флойд заметил, что некоторые студенты обмениваются записками. Сначала он хотел
# поставить им всем двойки, но в тот день профессор был добрым, а потому решил разделить студентов на две группы:
# списывающих и дающих списывать, и поставить двойки только первым.
#
# У профессора записаны все пары студентов, обменявшихся записками. Требуется определить, сможет ли он разделить
# студентов на две группы так, чтобы любой обмен записками осуществлялся от студента одной группы студенту другой
# группы.
# В первой строке находятся два числа N и M - количество студентов и количество пар студентов, обменивающихся записками
# (1<=N<=100, 0<=M<=2N(N−1)). Далее в M строках расположены описания пар студентов: два числа, соответствующие номерам
# студентов, обменивающихся записками (нумерация студентов идёт с 1). Каждая пара студентов перечислена не более одного
# раза.
# Необходимо вывести ответ на задачу профессора Флойда. Если возможно разделить студентов на две группы - выведите YES;
# иначе выведите NO.

def answer(n, pairs):
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
                    return 'NO'

    return 'YES'


def test0():
    test_data = ((3, [(1, 2), (1, 3)]), )
    for n, pairs in test_data:
        print(answer(n, pairs))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
