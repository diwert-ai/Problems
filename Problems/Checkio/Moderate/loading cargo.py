# https://py.checkio.org/ru/mission/loading-cargo/
# Вам дан список, сколько весят предметы для погрузки.
# Необходимо распределить их все так чтобы разница между
# общим весом в каждой руке была минимально возможной.
# Входные данные: Список весов предметов, как список (list)
# целых чисел (int).
# Выходные данные: Минимально возможная разница между весами
# в каждой руке, как целое число (int).

# вариация на тему дискретной задаче о рюкзаке (knapsack problem)


def checkio(data):
    S = sum(data)
    M = S//2
    N = len(data)
    F = [[0]*(N+1) for i in range(M+1)]
    for i in range(1, N+1):
        for k in range(1, M+1):
            if data[i-1] <= k:
                F[k][i] = max(F[k][i-1], data[i-1] + F[k-data[i-1]][i-1])
            else:
                F[k][i] = F[k][i-1]
    return abs(S - 2*F[M][N])
    
    
#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio([10, 10]) == 0, "1st example"
    assert checkio([10]) == 10, "2nd example"
    assert checkio([5, 8, 13, 27, 14]) == 3, "3rd example"
    assert checkio([5, 5, 6, 5]) == 1, "4th example"
    assert checkio([12, 30, 30, 32, 42, 49]) == 9, "5th example"
    assert checkio([1, 1, 1, 3]) == 0, "6th example"
    print('All done!')

