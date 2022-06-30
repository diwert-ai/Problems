#алгоритм поиска НОД
#из лекции Хирьянова https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7
#gcd - grand common divisor

import math

def gcd(a,b):
    assert a > 0
    return a if b == 0 else gcd(b,a%b)



def test():
    tests = [(1,1),(16,8),(74,2),(73,7),(34,17),(1024,256),(999,16),(5,12)]

    for a,b in tests:
        print(f'gcd({a},{b})={gcd(a,b)} math.gcd={math.gcd(a,b)}')

if __name__ == '__main__':
    test()
