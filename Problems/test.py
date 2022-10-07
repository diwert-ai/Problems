def checkio(buildings):
    n = len(buildings)
    builds = [(building[0], building[1], building[2] - building[0], building[4]) for building in buildings]
    builds.sort(key=lambda x: x[1])
    visible, widths = [False] * n, []

    def is_visible(inter):
        for w_int in widths:
            if inter[0] >= w_int[0] and inter[1] <= w_int[1]:
                return False
        return True

    def optimize_widths(inter):
        widths.sort(key=lambda x: x[0])
        for w_int in widths.copy():
            if w_int[1] < inter[0] or inter[1] < w_int[0]:
                continue
            inter = (min(inter[0], w_int[0]), max(inter[1], w_int[1]))
            widths.remove(w_int)
        widths.append(inter)

    def calc_widths(build_number):
        for k in range(build_number):
            if builds[build_number][3] <= builds[k][3]:
                widths.append(get_interval(builds[k]))
                optimize_widths(get_interval(builds[k]))

    def get_interval(bld):
        return bld[0], bld[0] + bld[2]

    for i, build in enumerate(builds):
        widths = []
        calc_widths(i)
        print(widths)
        if is_visible(get_interval(build)):
            visible[i] = True

    return sum(visible)


def test0():
    print(checkio([[1, 1, 4, 5, 3.5],
                   [2, 6, 4, 8, 5],
                   [5, 1, 9, 3, 6],
                   [5, 5, 6, 6, 8],
                   [7, 4, 10, 6, 4],
                   [5, 7, 10, 8, 3]]))
    print(checkio([[1, 1, 11, 2, 2],
                   [2, 3, 10, 4, 1],
                   [3, 5, 9, 6, 3],
                   [4, 7, 8, 8, 2]]))
    print(checkio([[1, 1, 3, 3, 6],
                   [5, 1, 7, 3, 6],
                   [9, 1, 11, 3, 6],
                   [1, 4, 3, 6, 6],
                   [5, 4, 7, 6, 6],
                   [9, 4, 11, 6, 6],
                   [1, 7, 11, 8, 3.25]]))
    print(checkio([[1, 1, 3, 3, 20],
                   [3, 4, 5, 6, 20],
                   [5, 1, 7, 3, 20],
                   [1, 7, 7, 9, 20]]))


def test1():
    assert checkio([
        [1, 1, 4, 5, 3.5],
        [2, 6, 4, 8, 5],
        [5, 1, 9, 3, 6],
        [5, 5, 6, 6, 8],
        [7, 4, 10, 6, 4],
        [5, 7, 10, 8, 3]
    ]) == 5, "First"
    assert checkio([
        [1, 1, 11, 2, 2],
        [2, 3, 10, 4, 1],
        [3, 5, 9, 6, 3],
        [4, 7, 8, 8, 2]
    ]) == 2, "Second"
    assert checkio([
        [1, 1, 3, 3, 6],
        [5, 1, 7, 3, 6],
        [9, 1, 11, 3, 6],
        [1, 4, 3, 6, 6],
        [5, 4, 7, 6, 6],
        [9, 4, 11, 6, 6],
        [1, 7, 11, 8, 3.25]
    ]) == 4, "Third"
    assert checkio([
        [0, 0, 1, 1, 10]
    ]) == 1, "Alone"
    assert checkio([
        [2, 2, 3, 3, 4],
        [2, 5, 3, 6, 4]
    ]) == 1, "Shadow"
    print('All asserts have successfully passed!')


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
