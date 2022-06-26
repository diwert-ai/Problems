#тест простоты числа из лекции Хирьянова: 
#https://www.youtube.com/watch?v=DvsCUI5FNnI&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=4


def is_simple_number(x):
    """
    Определяет, является ли число простым.
    x - целое положительное число.
    Если простое, то возвращает True, 
    а иначе - False.
    """
    divisor = 2
    while divisor < x:
        if x%divisor == 0:
            return False
        divisor+=1

    return True

def factorize_number(x):
    divisor = 2
    while x > 1:
        if x%divisor == 0:
            print(divisor,sep='')
            x //= divisor
        else:
            divisor+=1
    print('stop')

    return 'ok'

def test0():
    l = [998]
    for i in l:
        print(i,is_simple_number(i), factorize_number(i))

if __name__ == '__main__':
    test0()