# https://contest.yandex.ru/contest/49987/problems/I/
# Змей Горыныч оказался в лабиринте и хочет выбраться из него как можно скорее. К сожалению, после вчерашнего
# употребления кефира, левая голова Змея соображает плохо. Поэтому Змей Горыныч может поворачивать направо и идти прямо,
# но не может поворачивать налево и разворачиваться на месте. Помогите Змею Горынычу определить длину кратчайшего пути
# до выхода из лабиринта.
# В первой строке через пробел записаны числа r и c (4 ≤ r, c ≤ 20) - количество строк и столбцов в карте лабиринта.
# В каждой из следующих r строк записано по c символов, задающих эту карту. Символ S обозначает положение Змея Горыныча,
# символ F - точку выхода из лабиринта, символ X - стенку. Пробелами обозначены проходимые клетки. Гарантируется,
# что лабиринт окружен стенами. Перед началом движения Змей Горыныч может сориентироваться по любому из 4 направлений
# (вверх, вниз, влево или направо).
# В первой строке через пробел записаны числа r и c (4 ≤ r, c ≤ 20) - количество строк и столбцов в карте лабиринта.
# В каждой из следующих r строк записано по c символов, задающих эту карту. Символ S обозначает положение Змея Горыныча,
# символ F - точку выхода из лабиринта, символ X - стенку. Пробелами обозначены проходимые клетки. Гарантируется, что
# лабиринт окружен стенами. Перед началом движения Змей Горыныч может сориентироваться по любому из 4 направлений
# (вверх, вниз, влево или направо).

from heapq import heappop, heappush


def find_finish(r, c, maze):
    start, finish = None, None

    for i in range(r):
        line = maze[i]
        start_index = line.find('S')
        finish_index = line.find('F')
        if start_index > -1:
            start = (i, start_index)
        if finish_index > -1:
            finish = (i, finish_index)

    deltas = {'U': [(-1, 0), (0, 1)], 'D': [(1, 0), (0, -1)], 'R': [(0, 1), (1, 0)], 'L': [(0, -1), (-1, 0)]}
    dirs = {(-1, 0): 'U', (1, 0): 'D', (0, 1): 'R', (0, -1): 'L'}
    used = [[set() for _ in range(c)] for _ in range(r)]
    queue = [(0, 'U', start), (0, 'D', start), (0, 'L', start), (0, 'R', start)]

    while queue:
        dist, direction, position = heappop(queue)

        if position == finish:
            return dist
        pos_r, pos_c = position
        used[pos_r][pos_c].add(direction)

        for delta_r, delta_c in deltas[direction]:
            neighbour_r = pos_r + delta_r
            neighbour_c = pos_c + delta_c
            if 0 <= neighbour_r < r and 0 <= neighbour_c < c and maze[neighbour_r][neighbour_c] != 'X':
                new_dir = dirs[(delta_r, delta_c)]
                if new_dir not in (used[neighbour_r][neighbour_c]):
                    heappush(queue, (dist + 1, new_dir, (neighbour_r, neighbour_c)))

    return -1


def test0():
    test_data = ((10, 14, ['XXXXXXXXXXXXXX',
                           'X          XXX',
                           'X XFXXXXX    X',
                           'XXX   XX  XX X',
                           'X S          X',
                           'XX  XXXXXX X X',
                           'X        X X X',
                           'X X      X X X',
                           'XXX XX       X',
                           'XXXXXXXXXXXXXX']),
                 (10, 14, ['XXXXXXXXXXXXXX',
                           'X          FXX',
                           'X XXXX XX    X',
                           'XXXXXX XX  XXX',
                           'X            X',
                           'XXXXXX XXXXX X',
                           'X        X X X',
                           'X X      X X X',
                           'XXX XX      SX',
                           'XXXXXXXXXXXXXX']),
                 )
    for r, c, maze in test_data:
        print(find_finish(r, c, maze))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
