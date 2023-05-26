# https://contest.yandex.ru/contest/49613/problems/E/
# Требуется написать программу, определяющую, какие клавиши сломаются в процессе заданного варианта эксплуатации
# клавиатуры.
# Первая строка входных данных содержит одно целое число n – количество клавиш на клавиатуре.
# Вторая строка содержит n целых чисел – количество нажатий, выдерживаемых i-ой клавишей.
# Третья строка содержит целое число k – общее количество нажатий клавиш.
# Последняя строка содержит k целых чисел – последовательность нажатых клавиш.

def keys_status(limits, key_sequence):
    result = list()
    for key in key_sequence:
        limits[key - 1] -= 1

    for key_limit in limits:
        result.append('yes' if key_limit < 0 else 'no')

    return result


def test0():
    test_data = (([1, 50, 3, 4, 3], [1, 2, 3, 4, 5, 1, 3, 3, 4, 5, 5, 5, 5, 5, 4, 5]),
                 ([1, 1, 1], [1, 1, 2, 2, 3, 3]))

    for limits, key_sequence in test_data:
        print(*keys_status(limits, key_sequence))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
