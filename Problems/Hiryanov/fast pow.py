#быстрое возведение в степень
#из лекции Хирьянова https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7


def fast_pow(x,n):
    if n == 0:
        return 1

    if n%2 == 0:
        return fast_pow(x*x,n//2)
    else:
        return fast_pow(x*x,n//2)*x

def fast_pow_2(x,n):
    if n == 0:
        return 1
    

    if n%2 == 0:        
        return fast_pow_2(x*x,n//2)
    else:
        return fast_pow_2(x,n-1)*x


def test():
    print(fast_pow(2,200))

    print(fast_pow_2(2,200))

if __name__ == '__main__':
    test()
