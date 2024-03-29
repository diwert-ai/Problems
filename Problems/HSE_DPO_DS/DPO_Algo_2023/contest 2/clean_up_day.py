# https://contest.yandex.ru/contest/49329/problems/E/
# В классе учатся n человек. Классный руководитель получил указание направить на субботник r бригад по c человек в
# каждой.
#
# Все бригады на субботнике будут заниматься переноской бревен. Каждое бревно одновременно несут все члены одной
# бригады. При этом бревно нести тем удобнее, чем менее различается рост членов этой бригады.
#
# Числом неудобства бригады будем называть разность между ростом самого высокого и ростом самого низкого членов этой
# бригады (если в бригаде только один человек, то эта разница равна 0). Классный руководитель решил сформировать бригады
# так, чтобы максимальное из чисел неудобства сформированных бригад было минимально. Помогите ему в этом!


# метод бинарного поиска по ответу
def check_mid(diffs, r, c, mid):
    finds, i = 0, 0

    while i < len(diffs):
        if diffs[i] <= mid:
            finds += 1
            i += c
        else:
            i += 1

        if finds == r:
            return True

    return False


def minmax_diff(heights, r, c):
    heights.sort()
    left, right = 0, heights[-1] - heights[0]
    diffs = [heights[i + c - 1] - heights[i] for i in range(len(heights) - c + 1)]
    while left < right:
        mid = (left + right) // 2
        if check_mid(diffs, r, c, mid):
            right = mid
        else:
            left = mid + 1
    return right


def test0():
    test_data = (([3, 5, 5, 6, 15], 2, 2),
                 ([170, 205, 225, 190, 260, 130, 225, 160], 2, 3),
                 ([984384487, 56495279, 71889363, 621081665, 547627171, 640272482, 313639755, 314358004, 414135504], 3,
                  3),
                 ([649247234, 960108144, 865567932, 937129087, 191500659, 907092244, 264414918, 939965614, 659512652,
                  610633006, 748987003, 965400939, 144204064, 785096266, 338621548, 812248988, 755723863, 128928093,
                  784403302, 554444068, 987572241, 355948104, 271817718, 497692750, 364484640, 506445744, 907295550,
                  842554765, 830152853, 228552614, 412330113, 378375448, 622466426, 455983598, 389193718, 223734203,
                  41638987, 516215594, 922820558, 200878677, 113281811, 49407040, 911654011, 482805423, 648903163,
                  73662886, 169884834, 612582907, 390856094, 582477145], 21, 1)
                 )

    for heights, r, c in test_data:
        print(minmax_diff(heights, r, c))


def test1():
    pass


if __name__ == '__main__':
    tests = (test0, test1)
    for test in tests:
        test()
