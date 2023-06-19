# https://contest.yandex.ru/contest/50252/problems/B/
# Реализовать алгоритм Кнута - Морриса - Пратта для поиска подстроки в строке.
# Первая строка – s (0≤∣s∣≤1000) – строка, вхождения которой ищем.
# Вторая строка – t (0≤∣t∣≤10^7) – текст, в котором ищутся вхождения строки.
# Гарантируется, что строки состоят только из букв латинского алфавита.
# На первой строке выходного файла – количество вхождений строки в текст.
#
# Гарантируется, что количество вхождений строки в текст не превышает 10^6
# На каждой следующей строке выходного файла номера позиций (индексирование ведётся с 0), с которых начинаются очередные
# вхождения строки. За последним номером также следует перенос строки.

def kmp(p, s):
    s = p + '#' + s
    n = len(s)
    m = len(p)
    prefix = [0] * n
    cur_p = 0
    result = []

    for i in range(1, n):
        while cur_p > 0 and s[cur_p] != s[i]:
            cur_p = prefix[cur_p - 1]
        if s[i] == s[cur_p]:
            cur_p += 1
        if cur_p == m:
            result.append(i - 2 * m)
        prefix[i] = cur_p

    return len(result), result


def test0():
    test_data = (('bc', 'dcbbabcaababcccbcbba'), ('dad', 'dcbdbdcabbcdcddcacaa'))
    for p, s in test_data:
        print(*kmp(p, s))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
