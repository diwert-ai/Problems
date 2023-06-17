# https://contest.yandex.ru/contest/50168/problems/G/
# За билетами на премьеру нового мюзикла выстроилась очередь из N человек, каждый из которых хочет купить 1 билет. На
# всю очередь работала только одна касса, поэтому продажа билетов шла очень медленно, приводя «постояльцев» очереди в
# отчаяние. Самые сообразительные быстро заметили, что, как правило, несколько билетов в одни руки кассир продаёт
# быстрее, чем когда эти же билеты продаются по одному. Поэтому они предложили нескольким подряд стоящим людям отдавать
# деньги первому из них, чтобы он купил билеты на всех.
#
# Однако для борьбы со спекулянтами кассир продавала не более 3-х билетов в одни руки, поэтому договориться таким
# образом между собой могли лишь 2 или 3 подряд стоящих человека.
#
# Известно, что на продажу i-му человеку из очереди одного билета кассир тратит Ai секунд, на продажу двух билетов — Bi
# секунд, трех билетов — Ci секунд. Напишите программу, которая подсчитает минимальное время, за которое могли быть
# обслужены все покупатели.
#
# Обратите внимание, что билеты на группу объединившихся людей всегда покупает первый из них. Также никто в целях
# ускорения не покупает лишних билетов (то есть билетов, которые никому не нужны).

# На вход программы поступает сначала число N — количество покупателей в очереди (1≤N≤5000). Далее идет N троек
# натуральных чисел Ai, Bi, Ci. Каждое из этих чисел не превышает 3600. Люди в очереди нумеруются, начиная от кассы.

# Требуется вывести одно число — минимальное время в секундах, за которое могли быть обслужены все покупатели.

def answer(triplets):
    n = len(triplets)
    a = [0] * 5001
    b = [0] * 5001
    c = [0] * 5001
    r = [0] * 5001

    for i in range(1, n + 1):
        a[i], b[i], c[i] = triplets[i-1]

    r[1] = a[n]
    r[2] = min(a[n] + a[n - 1], b[n - 1])
    r[3] = min(c[n - 2], a[n] + b[n - 2], a[n] + a[n - 1] + a[n - 2])

    for i in range(4, n + 1):
        r[i] = min(a[n - i + 1] + r[i - 1], b[n - i + 1] + r[i - 2], c[n - i + 1] + r[i - 3])

    return r[n]


def test0():
    test_data = (((5, 10, 15), (2, 10, 15), (5, 5, 5), (20, 20, 1), (20, 1, 1)),
                 ((3, 4, 5), (1, 1, 1)),
                 ((1, 2, 3),))
    for triplets in test_data:
        print(answer(triplets))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
