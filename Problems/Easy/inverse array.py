#функция инвертирования массива
#из лекции Хирьянова https://www.youtube.com/watch?v=3I6OjxoeSS8&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=5

def invert_array(A:list, N:int):
    """
    Обращение массива (поворот задом-наперед)
    в рамках индексов от 0 от N-1
    """

    for i in range(N//2):
        A[i],A[N-i-1] = A[N-i-1],A[i]


def test0():
    l = [1,2,3,4,5,6,7,8,9,10,10]
    print(l)
    invert_array(l, 5)
    print(l)

if __name__ == '__main__':
    test0()
