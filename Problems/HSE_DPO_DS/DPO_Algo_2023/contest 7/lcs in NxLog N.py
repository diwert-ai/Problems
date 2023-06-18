# https://contest.yandex.ru/contest/50168/problems/R/
# Числовая последовательность задана рекуррентной формулой: ai+1 = (k * ai + b) mod m. Найдите длину её наибольшей
# возрастающей подпоследовательности. Программа получает на вход пять целых чисел: длину последовательности n
# (1 ≤ n ≤ 105), начальный элемент последовательности a1, параметры k, b, m для вычисления последующих членов
# последовательности (1 ≤ m ≤ 104, 0 ≤ k < m, 0 ≤ b < m, 0 ≤ a1 < m). Требуется вывести длину наибольшей возрастающей
# подпоследовательности данной последовательности.

def lcs_n_log_n(n, a0, k, b, m):
    dp = [-1] * n
    array = [a0] * n

    for i in range(1, n):
        array[i] = (k * array[i - 1] + b) % m

    dp[0] = array[0]
    answer = 1

    def bin_search():
        right = answer - 1
        if ai > dp[right]:
            return right + 1
        left = 0
        while left < right:
            mid = (left + right) // 2
            if ai > dp[mid]:
                left = mid + 1
            else:
                right = mid
        return left

    for i in range(1, n):
        ai = array[i]
        j = bin_search()
        dp[j] = ai
        answer = max(answer, j + 1)

    return answer


def test0():
    test_data = ((5, 41, 2, 1, 100),
                 (7, 1, 2, 1, 10),
                 (7, 2, 2, 1, 10))
    for n, a0, k, b, m in test_data:
        print(lcs_n_log_n(n, a0, k, b, m))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
