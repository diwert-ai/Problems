# https://contest.yandex.ru/contest/49987/problems/H/
# Даны N точек, занумерованных числами 1, 2, ..., N. От каждой точки с меньшим номером к каждой точке с большим номером
# ведет стрелка красного или синего цвета. Раскраска стрелок называется однотонной, если нет двух таких точек A и B, что
# от A до B можно добраться как только по красным стрелкам, так и только по синим.
#
# Ваша задача — по заданной раскраске определить, является ли она однотонной.
# В первой строке входных данных содержится единственное число N (3 ≤ N ≤ 5000).
# В следующих N–1 строках идет описание раскраски. В (i+1)-й строке записано (N–i) символов R (красный) или B (синий),
# соответствующих цвету стрелок, выходящих из точки i и входящих в точки (i+1), (i+2), ..., N соответственно.

def answer(n, color_lines):
    red_graph = {i: set() for i in range(n)}
    blue_graph = {i: set() for i in range(n)}

    for i in range(n - 1):
        for j, char in enumerate(color_lines[i], 1):
            if char == 'R':
                red_graph[i].add(i + j)
            elif char == 'B':
                blue_graph[i].add(i + j)

    for i in range(n):
        used_red = set()
        used_red.add(i)
        stack = [i]
        while stack:
            vertex = stack.pop()
            for neighbour in red_graph[vertex]:
                if neighbour not in used_red:
                    used_red.add(neighbour)
                    stack.append(neighbour)

        used_red.discard(i)
        used_blue = set()
        used_blue.add(i)
        stack = [i]
        while stack:
            vertex = stack.pop()
            for neighbour in blue_graph[vertex]:
                if neighbour not in used_blue:
                    if neighbour in used_red:
                        return 'NO'
                    used_blue.add(neighbour)
                    stack.append(neighbour)

    return 'YES'


def test0():
    test_data = ((3, ['RB', 'R']),
                 (5, ['RBRB', 'BBB', 'RR', 'B']))
    for n, color_lines in test_data:
        print(answer(n, color_lines))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
