# https://contest.yandex.ru/contest/49847/problems/C/
# Фирма OISAC выпустила новую версию калькулятора. Этот калькулятор берет с пользователя деньги за совершаемые
# арифметические операции. Стоимость каждой операции в долларах равна 5% от числа, которое является результатом
# операции. На этом калькуляторе требуется вычислить сумму N натуральных чисел (числа известны).
# Напишите программу, которая будет определять, за какую минимальную сумму денег можно найти сумму данных N чисел.

from heapq import heapify, heappop, heappushpop


def calc_cost(heap):
    cost, n = 0, len(heap)
    heapify(heap)
    tmp = heappop(heap)
    for _ in range(1, n):
        min_sum = tmp + heappop(heap)
        cost += min_sum * 0.05
        tmp = heappushpop(heap, min_sum)

    return cost


def test0():
    arrays = ([10, 11, 12, 13], [1, 2, 5, 6, 12, 13])
    for array in arrays:
        print(f'{calc_cost(array):.2f}')


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
