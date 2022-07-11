#пример: обратная польская запись
#из лекции Хирьянова https://www.youtube.com/watch?v=rEPggzaPoUw&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=12

from mystack import MyStack

def rpn(expression: list):
    """алгоритм вычисления выражений в постфиксной нотации
    >>> rpn([1,2,'+'])
    3
    >>> rpn([2,3,4,'+','*'])
    14
    >>> rpn([2,6,'*',7,'+',8,'-'])
    11
    >>> rpn([1,2,3,4,5,6,7,8,'+','-','*','+','/','+','*'])
    1.9268292682926829
    >>> rpn([1,2,3,'*','+',2,3,4,'+','+','-'])
    -2
    >>> rpn([8,2,5,'*','+',1,3,2,'*','+',4,'-','/'])
    6.0
    >>> rpn([1,2,'#'])
    unexpected token: #
    """
    
    st = MyStack()
    for token in expression:
        if str(token).isdigit():
            st.push(token)
        else:
            y = st.pop()
            x = st.pop()
            if token == '+':
                z = x + y
            elif token == '-':
                z = x - y
            elif token == '*':
                z = x * y
            elif token == '/':
                z = x / y
            else:
                print(f'unexpected token: {token}')
                return None

            st.push(z)

    return st.pop()

def test0():
    import doctest
    doctest.testmod(verbose=True)

def test1():
    rpn([1,2,'#'])

if __name__ == '__main__':
    test0()


   

