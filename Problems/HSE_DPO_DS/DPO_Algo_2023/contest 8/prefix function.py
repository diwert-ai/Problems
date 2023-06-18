# https://contest.yandex.ru/contest/50252/problems/A/
# Дана строка s, состоящая из строчных букв латинского алфавита. Будем считать, что элементы строки нумеруются от 0 до
# ∣s∣−1. Требуется для всех i от 0 до ∣s∣−1 вычислить её префикс-функцию π[i]. Одна строка s (1≤∣s∣≤10^6), состоящая из
# строчных букв латинского алфавита. Выведите ∣s∣ чисел – значения префикс-функции для каждой позиции, разделённые
# пробелом.

def answer(s):
    n = len(s)
    prefix = [0] * n
    cur_p = 0

    for i in range(1, n):
        while cur_p > 0 and s[cur_p] != s[i]:
            cur_p = prefix[cur_p - 1]
        if s[i] == s[cur_p]:
            cur_p += 1
        prefix[i] = cur_p

    return prefix


def test0():
    test_data = ('abcabcabc', 'abracadabra')
    for s in test_data:
        print(*answer(s))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
