#последовательность фибоначи
#из лекции  Хирьянова https://www.youtube.com/watch?v=EdhN_gEDfUM&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=10

def fib(n):
    #рекурсивный подход с ассимптотикой по времени O(F(N)) - эспоненциальная
    if n < 2:
        return n

    return fib(n-1)+fib(n-2)


def fib_cycle(n):
    #обычный цикл. О(N) время O(1) память
    if n < 2:
        return n
    f_0 = 0
    f_1 = 1
    ret = 0
    for i in range(n-1):
        ret = f_0 + f_1
        f_0 = f_1
        f_1 = ret

    return ret

def fib_dp(n):
    #динамическое программирование - О(N) время О(N) - память
    dp = [0,1]+[0]*(n-1)
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]

def test0():
    n = [0,1,2,3,4,5,6,7,8]
    for k in n:
        print(fib(k), end = ' ')
    print('')
    
    for k in n:
        print(fib_cycle(k), end = ' ')
    print('')

    for k in n:
        print(fib_dp(k), end = ' ')
    print('')




if __name__ == '__main__':
    test0()
