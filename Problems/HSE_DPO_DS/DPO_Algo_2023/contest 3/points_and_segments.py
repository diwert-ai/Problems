# https://contest.yandex.ru/contest/49613/problems/B/
# Даны два множества: отрезки на прямой и точки. Для каждой точки из второго множества, определите количество отрезков,
# которым она принадлежит. Точка считается принадлежащей отрезку, если она находится внутри него или на границе.
# Задача из курса «Алгоритмы: теория и практика. Методы»: https://stepik.org/course/217/syllabus

def count_segments(segments, points):
    count, m, events = 0, len(points), list()
    results = [0] * m

    for a, b in segments:
        events.append((a, -1))
        events.append((b, m))

    for index in range(m):
        events.append((points[index], index))

    events.sort()

    for _, index in events:
        if index in (-1, m):
            count += (1 if index == -1 else -1)
        else:
            results[index] = count

    return results


def test0():
    test_data = ((((5, 5), (1, 3), (2, 4), (3, 10), (4, 5), (1, 3)), (1, 2, 3, 4, 5)),
                 (((3, 3), (1, 1), (2, 2), (3, 3)), (-1, 0, 1)),
                 )
    for segments, points in test_data:
        print(*count_segments(segments, points))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
