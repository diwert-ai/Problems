import itertools


def rpn(expression: list):
    """функция вычисления выражений в постфиксной нотации
    """
    st = []
    for token in expression:
        if str(token).isdigit():
            st.append(token)
        else:
            if st == []:
                return None
            y = st.pop()

            if st == []:
                return None
            x = st.pop()

            if token == '+':
                z = x + y
            elif token == '-':
                z = x - y
            elif token == '*':
                z = x * y
            elif token == '/':
                if y == 0:
                    return None
                z = x / y
            else:
                print(f'unexpected token: {token}')
                return None

            st.append(z)

    return st.pop() if len(st)==1 else None

def gen_ordered_permutations(l1:list,l2:list,m:int,prefix=[]):
    """генератор перестановок элементов из двух списков l1 и l2,
       сохраняющих порядок следования элементов в этих списках:
       l1=[1,2,3] l2=['+','-'] -> [1,2,'+',3,'-']; ['+',1,2,'-',3] и тд
       m - глубина рекурсии = len(l1)+len(l2)
       prefix - возвращаемая перестановка
    """ 
    if m == 0:
        yield prefix
    if len(l1) > 0:
        yield from gen_ordered_permutations(l1[1:],l2,m-1,prefix+[l1[0]])
    if len(l2) > 0:
        yield from gen_ordered_permutations(l1,l2[1:],m-1,prefix+[l2[0]])

def gen_groups(t,m,prefix=[]):
    '''генератор группировок чисел
       t = '123456' -> [1,2,3,4,5,6], [12,3,4,5,6], [1,234,5,6] и тд
    '''
    if m == 0:
        yield prefix
    
    for i in range(m):
        if len(t) > i:
            yield from gen_groups(t[i+1:],m-i-1,prefix+[int(t[0:i+1])])


def find100(t):
    if int(t) == 100:
        return [100], True

    operations = ['+','-','*','/']
    for combination in gen_groups(t,len(t)):
        if len(combination) == 1:
            continue
        for i in itertools.product(operations,repeat=len(combination)-1):
            l1 = combination[2:]
            l2 = list(i)
            for j in gen_ordered_permutations(l1,l2,len(l1)+len(l2)):
                rpn_expression = combination[0:2]+list(j)
                if rpn(rpn_expression) == 100:
                    return rpn_expression,True    
    return None,False


def test0():
    #tests = [[2,7,1,3,5,3],
    #         [5,9,3,3,4,7],
    #         [7,0,7,4,0,9],
    #         [5,9,5,3,47],
    #         [0,0,0,0,0,0],
    #         [5,6,1,7,0,9],
    #         [5,9,3,34,7]]
    
    tests = ['600500',
             '001010',
             '101000',
             '000100',
             '271353',
             '593347',
             '707409',
             '595347',
             '000000',
             '561709',
             '593347']

    for i,test in enumerate(tests):
        print(f'test#{i}: {test} {find100(test)}')


if __name__ == '__main__':
    test0()


#print(rpn([2,7,1,3,'/',5,'-',3,'*','*','-']))

#s = [1,2,3,4]
#b = ['+','*','-','/','+']




#gen  = gen_per(s,b,len(s)+len(b))

#for i,k in enumerate(gen):
#    print(i+1, k)
