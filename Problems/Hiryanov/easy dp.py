# простые примеры на дин программирование
# из лекции Хирьянова https://www.youtube.com/watch?v=EdhN_gEDfUM&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=10

# Задача про кузнечика
# кузнечик из точки 1 на числовой прямой умеет прыгать либо на +1, либо на +2
# сколько способов есть у кузнечика попасть в точку n
# в точку n кузнечик может попасть либо из точки n-1,либо из точки n-2
# тогда К_n = K_{n-1} + K_{n-2}. решается по аналогии с последовательностью Фибоначчи.

def traj_num(n: int):
    # k[0]=0 - в точку 0 ноль способов попасть
    k = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        k[i] = k[i-2] + k[i-1]

    return k, k[n], n


# пусть дополнительно есть запрещенные точки для посещения и кузнечик может прыгать 
# дополнительно еще и на +3
def traj_count(n: int, allowed: list):
    # allowed - булевский массив, allowed[i] - True, если точку i разрешено посещать
    # и False в противном случае
    k = [0, 1, int(allowed[2])]+[0]*(n-2)
    for i in range(3, n+1):
        if allowed[i]:
            k[i] = k[i-1]+k[i-2]+k[i-3]

    return k, k[n], n


# теперь пусть минимальная стоимость достижения точки n - cost[n]
# пусть посещение точки i стоит price[i]
# тогда cost[i] = price[i] + min(cost[i-1],cost[i-2], cost[i-3])
def traj_minimum_cost(n: int, allowed: list, price: list):
    cost = [0, 1, 0 if allowed[2] else float('inf')]+[float('inf')]*(n-2)
    for i in range(3, n+1):
        if allowed[i]:
            cost[i] = price[i] + min(cost[i-1], cost[i-2], cost[i-3])

    return cost, cost[n], n


def test0():
    n = 10
    allowed = [False if i % 5 + i % 7 == 4 else True for i in range(n+1)]
    price = [i % 2 + 2 for i in range(n+1)]
    print(traj_num(n))
    print(traj_count(n, allowed))
    print(traj_minimum_cost(n, allowed, price))
                        

if __name__ == '__main__':
    test0()
