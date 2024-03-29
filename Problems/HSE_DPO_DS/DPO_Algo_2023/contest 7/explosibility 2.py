# https://contest.yandex.ru/contest/50168/problems/E/
# При переработке радиоактивных материалов образуются отходы трех видов — особо опасные (тип A), неопасные (тип B) и
# совсем неопасные (тип C). Для их хранения используются одинаковые контейнеры. После помещения отходов в контейнеры
# последние укладываются вертикальной стопкой. Стопка считается взрывоопасной, если в ней подряд идет более одного
# контейнера типа A. Стопка считается безопасной, если она не является взрывоопасной. Для заданного количества
# контейнеров N определить число безопасных стопок.
# Вывод: одно число — количество безопасных вариантов формирования стопки.

def answer(n):
    a = [1] * 21
    b = [1] * 21
    c = [1] * 21

    for i in range(1, n):
        a[i] = b[i - 1] + c[i - 1]
        b[i] = c[i] = a[i] + a[i - 1]

    return a[n - 1] + b[n - 1] + c[n - 1]


def test0():
    test_data = (1, 2, 3, 4, 5, 20)
    for n in test_data:
        print(answer(n))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
