# https://contest.yandex.ru/contest/49329/problems/C/
# Найдите такое число x^2 + sqrt(x) = C с точностью не менее 6 знаков после точки.
#
# Формат ввода.
# В единственной строке содержится вещественное число 1.0 <= C <= 10^10.
#
# Формат вывода.
# Выведите одно число — искомый x.
#
# Примечания.
# Использовать стандартные методы для поиска - нельзя!!! Решать с использованием вещественного бинарного поиска.

def func(x):
    return x * x + x ** 0.5


def get_bounds(f, c):
    right = 1
    while f(right) < c:
        right *= 2
    return 0.0, float(right)


def find_root(f, epsilon, c):
    left, right = get_bounds(f, c)
    while right - left > epsilon:
        mid = (right + left) / 2.0
        if f(mid) < c:
            left = mid
        else:
            right = mid

    return (right + left) / 2.0


def test0():
    test_c = (2, 18, 20, 30, 100)
    eps = 0.0000001
    for c in test_c:
        print(find_root(func, eps, c))


def test1():
    eps = 0.0000001
    for _ in range(3):
        c = float(input())
        print(find_root(func, eps, c))


if __name__ == '__main__':
    tests = (test0, test1)
    for test in tests:
        test()
