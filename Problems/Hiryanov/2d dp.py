﻿# Пример двумерных задач на динамическое программирование
# из лекции Хирьянова https://www.youtube.com/watch?v=m4HOkVeN4Mo

# Шахматный король живет на доске NxM и может совершать
# ходы: вправо на 1 и вниз на 1.
# Сколько разных способов есть у короля, чтобы добраться
# из клетки (1,1) в клетку (N,M).
# Пусть K_{i,j} - кол-во способов достичь клетки (i,j),
# тогда K_{i,j} = K_{i-1,j} + K_{i,j-1}.


def king_traj_count(n, m):
    # Создаем таблицу n+1 строк на m+1 столбцов.
    # Дополнительные строка и столбец нужны для
    # удобства (барьерные элементы).
    # f_{i,j} = f[i][j]

    f = [[0]*(m+1) for _ in range(n+1)]

    # f_{1,1} = 1 по условию
    f[1][1] = 1
    
    # заполняем таблицу f
    for i in range(1, n+1):
        for j in range(1, m+1):
            # элемент f_{1,1} не вычисляем
            if i == 1 and j == 1:
                continue

            f[i][j] = f[i][j-1] + f[i-1][j]

    return f, f[-1][-1]


# Наибольшая общая подпоследовательность.
# Пусть a, b - одномерные массивы чисел
# длины N и M соответственно.
# Пусть f_{i,j} - длина наибольшей возможной подпоследовательности
# частей a и b: a[0:i] - часть a из первых его i элементов и
# b[0:j] - аналогичная часть b.
# f_{i,j} = f_{i-1,j-1} + 1, если  a[i-1]==b[j-1]
#        = max(f_{i,j-1},f_{i-1,j}) если a[i-1]!=b[j-1]
#
# f_{0,j} = f_{i,0} = 0  для всех i,j
def lcs(a, b):
    n = len(a)+1
    m = len(b)+1
    f = [[0]*m for _ in range(n)]

    for i in range(1, n):
        for j in range(1, m):
            if a[i-1] == b[j-1]:
                f[i][j] = f[i-1][j-1] + 1
            else:
                f[i][j] = max(f[i][j-1], f[i-1][j])

    return f[-1][-1]


# Наибольшая возрастающая подпоследовательность.
# 1-й подход: свести к предыдущей задаче: lcs(a,sorted(a)) -
# тогда O(N^2) сложность по времени O(N^2) - сложность по памяти, где N = len(a)
# но так можно сделать, только если речь идет о неубывающей подпоследовательности.
# Если ищется строго возрастающая подпоследовательность, то такой подход не сработает.

# 2-й подход:
# заметим, что для самого короткого среза a[0:i], в котором лежит искомая НВП,
# верно, что a[i-1] (последний элемент среза) принадлежит НВП и является
# максимальным элементом НВП.
# Поэтому пусть f_i - длина НВП для среза a[0:i]
# при этом это такая НВП, которая заканчивается и содержит элемент a[i-1].
# Тогда f_i = max(f_j)+1 при j<i и a[i-1]>a[j-1], либо 0 если условия не выполнены.
# Длина искомой НВП в таком случае будет max(f)
def gis(a):
    n = len(a)+1
    f = [0]*n
    m = 0
    for i in range(1, n):
        m = 0
        for j in range(1, i):
            if f[j] > m and a[i-1] > a[j-1]:
                m = f[j]
        f[i] = m + 1
        if f[i] > m:
            m = f[i]
    return m


def test0():
    print(king_traj_count(3, 5))


def test1():
    print(lcs([0, 0, 1, 0, 0, 0, 5, 0, 0, 0, 6, 6, 6, 6, 6], [1, 2, 3, 5, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6]))


def test2():
    a = [-1, 10, 7, 3, 4, 5, 100, 200, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(lcs(a, sorted(a)))
    print(gis(a))


if __name__ == '__main__':
    test2()
