# https://py.checkio.org/en/mission/buildings-visibility/
def checkio(buildings):
    num_visible_builds = 0
    builds = [(building[0], building[1], building[2] - building[0], building[4]) for building in buildings]
    builds.sort(key=lambda x: x[1])

    def get_interval(bld):
        return bld[0], bld[0] + bld[2]

    def add_interval(inter):
        for w_int in non_overlapped_intervals.copy():
            if not (w_int[1] < inter[0] or inter[1] < w_int[0]):
                inter = (min(inter[0], w_int[0]), max(inter[1], w_int[1]))
                non_overlapped_intervals.remove(w_int)
        non_overlapped_intervals.append(inter)

    def gen_non_overlapped_intervals(build_number):
        for k in range(build_number):
            if builds[build_number][3] <= builds[k][3]:
                add_interval(get_interval(builds[k]))

    def is_visible(inter):
        for w_int in non_overlapped_intervals:
            if inter[0] >= w_int[0] and inter[1] <= w_int[1]:
                return False
        return True

    for i, build in enumerate(builds):
        non_overlapped_intervals = []
        gen_non_overlapped_intervals(i)
        if is_visible(get_interval(build)):
            num_visible_builds += 1

    return num_visible_builds


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
    print(checkio([[1, 1, 8, 2, 3],
                   [2, 3, 7, 4, 6],
                   [3, 5, 6, 6, 5]]))
    print(checkio([[1, 1, 8, 2, 3],
                   [2, 3, 7, 4, 6],
                   [2.5, 5, 6.5, 6, 4],
                   [3, 7, 6, 8, 5]]))


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
    assert checkio([[1, 1, 8, 2, 3],
                    [2, 3, 7, 4, 6],
                    [3, 5, 6, 6, 5]]) == 2, "Chain"
    assert checkio([[1, 1, 8, 2, 3],
                    [2, 3, 7, 4, 6],
                    [2.5, 5, 6.5, 6, 4],
                    [3, 7, 6, 8, 5]]) == 2, "More chain!"
    print('All asserts have successfully passed!')


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
