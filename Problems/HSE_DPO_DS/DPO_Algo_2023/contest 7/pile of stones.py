# https://contest.yandex.ru/contest/50168/problems/N/
# У вас есть несколько камней известного веса w_1, …, w_n. Напишите программу, которая распределит камни в две кучи так,
# что разность весов этих двух куч будет минимальной. Ввод содержит количество камней n (1 ≤ n ≤ 20) и веса камней w_1,
# …, w_n (1 ≤ w_i ≤ 1000) – целые, разделённые пробельными символами. Ваша программа должна вывести одно число –
# минимальную разность весов двух куч.

def answer(weights):
    n = len(weights)
    result = sum(weights)

    for i in range(2 ** n):
        mask = f'{i:0{n}b}'
        w0 = w1 = 0
        for pos, val in enumerate(mask):
            if val == '0':
                w0 += weights[pos]
            else:
                w1 += weights[pos]

        result = min(result, abs(w1 - w0))

    return result


def test0():
    test_data = ((5, 8, 13, 27, 14), )
    for weights in test_data:
        print(answer(weights))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
