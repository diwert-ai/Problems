# https://contest.yandex.ru/contest/49613/problems/A/
# В одномерном массиве, заполненном произвольными целыми числами, за один проход найдите непрерывный кусок, сумма чисел
# в котором максимальна.
#
# Примечание. Фактически требуется найти такие i и j (i ≤ j), что сумма всех элементов массива от a_i до a_j
# включительно будет максимальна.

def array_sum(array):
    max_sum = last_sum = left_max = right_max = left = 0

    for right, a_r in enumerate(array):
        if last_sum > 0:
            last_sum += a_r
        else:
            last_sum, left = a_r, right

        if last_sum > max_sum:
            left_max, right_max, max_sum = left, right, last_sum

    return left_max, right_max


def test0():
    arrays = ([-5, -9, -6],
              [-5, -8, -9, 7, 4, -1, 6, 8, -1, 1])

    for array in arrays:
        print(*array_sum(array))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
