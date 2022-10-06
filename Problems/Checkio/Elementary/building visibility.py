# https://py.checkio.org/en/mission/buildings-visibility/
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
            if not (w_int[1] < inter[0] or inter[1] < w_int[0]):
                inter = (min(inter[0], w_int[0]), max(inter[1], w_int[1]))
                widths.remove(w_int)
        widths.append(inter)

    def get_interval(bld):
        return bld[0], bld[0] + bld[2]

    for i, build in enumerate(builds):
        interval = get_interval(build)
        if is_visible(interval):
            optimize_widths(interval)
            visible[i] = True

    builds_visible = {build: i for i, build in enumerate(builds) if visible[i]}
    builds_invisible = {build: i for i, build in enumerate(builds) if not visible[i]}

    def behind(uv_b, v_b):
        inter1 = get_interval(uv_b)
        inter2 = get_interval(v_b)
        return not (inter1[1] < inter2[0] or inter2[1] < inter1[0])

    for iv_build in builds_invisible:
        iv_index = builds_invisible[iv_build]
        for v_build in builds_visible:
            v_index = builds_visible[v_build]
            if iv_index > v_index and behind(iv_build, v_build) and iv_build[3] > v_build[3]:
                visible[iv_index] = True

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
    # todo: исправить ошибку с примером ниже
    assert checkio([[1, 1, 8, 2, 3],
                    [2, 3, 7, 4, 6],
                    [3, 5, 6, 6, 5]]) == 2


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
