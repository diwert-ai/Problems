# https://contest.yandex.ru/contest/50168/problems/D/
# При переработке радиоактивных материалов образуются отходы двух видов — особо опасные (тип A) и неопасные (тип B).
# Для их хранения используются одинаковые контейнеры. После помещения отходов в контейнеры последние укладываются
# вертикальной стопкой. Стопка считается взрывоопасной, если в ней подряд идет более одного контейнера типа A. Стопка
# считается безопасной, если она не является взрывоопасной. Для заданного количества контейнеров N определить количество
# возможных типов безопасных стопок.
# Ввод: одно число 1 <= N <= 20. Вывод: одно число — количество безопасных вариантов формирования стопки.

def answer(n):
    fibo = [1] * 21

    for i in range(2, n + 1):
        fibo[i] = fibo[i - 1] + fibo[i - 2]

    return fibo[n] + fibo[n - 1]


def test0():
    test_data = (1, 2, 3, 4, 5, 20)
    for n in test_data:
        print(answer(n))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
