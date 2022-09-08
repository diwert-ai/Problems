# алгоритм поиска НОД
# из лекции Хирьянова https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7
# gcd - grand common divisor

import math


# a,b > 0
def gcd_p(a, b):
    return a if b == 0 else gcd_p(b, a % b)


# a,b любого знака
def gcd(a, b):
    a = abs(a)
    b = abs(b)
    return gcd_p(b, a % b)


def test():
    tests = [(1, 1), (-16, -8), (74, 2), (-73, 7), (34, 17), (1024, 256), (999, 16), (5, 12), (12, -6), (-100, 200),
             (-200, -13)]

    for a, b in tests:
        print(f'gcd({a}, {b}) = {gcd(a, b)} : math.gcd = {math.gcd(a, b)}')


if __name__ == '__main__':
    test()
