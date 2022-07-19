'''
Задача https://py.checkio.org/en/mission/mathematically-lucky-tickets/
The "Mathematically lucky tickets" concept is similar to the idea of the Russian "Lucky tickets". It refers to the old public transport tickets that had 6-digit numbers printed on them.

You are given a ticket number and the combination of its digits can become a mathematical expression by following these rules.

    1. The digits of the number can be split into groups of numbers.
    2. You cannot change the order of groups or digits.
    3. Each group is treated as a one integer number. (1 and 2 would become 12, etc.)
    4. Operational signs (+, -, * and /) are placed between the groups.
    5. Parenthesis are placed around subexpressions to eliminate any ambiguity
    in the evaluation order.

For example:

    * 238756 -> (2 * (38 + ((7 + 5) * 6)))
    * 000859 -> (0 + (00 + (8 + (5 + 9))))
    * 561403 -> (5 * (6 + (1 + (40 / 3))))

The ticket is considered mathematically lucky if no combination of its digits evaluates to 100. For example:

    * 000000 is obviously lucky, no matter which combination you construct it always
    evaluates to zero,
    * 707409 and 561709 are also lucky because they cannot evaluate to 100
    * 595347 is not lucky: (5 + ((9 * 5) + (3 + 47))) = 100
    * 593347 is not lucky: (5 + ((9 / (3 / 34)) - 7)) = 100
    * 271353 is not lucky: (2 - (7 * (((1 / 3) - 5) * 3))) = 100

The combination has to evaluate to 100 exactly to be counted as unlucky. Fractions can occur in intermediate calculations (like in above examples for 593347 and 271353) but the result must be an integer.

Task: Given a 6-digit number of the ticket, the program should determine whether it is mathematically lucky or not.

Input: 6 digits as a string.

Output: Is it mathematically lucky or not as a boolean.

Example:

checkio('000000') == True
checkio('707409') == True
checkio('595347') == False
checkio('271353') == False
1
2
3
4
How it is used: This is a nice game to improve mind-calculation skills. If you have coder or math-geek friends, then you can give them this as a challenge. Who’s code will check digits faster than the others? After solving this task you will have the skills to cheat! ;-)

Precondition: |digits| == 6
'''

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

def gen_ordered_permutations(l1:list,l2:list,m:int,prefix=None):
    """генератор перестановок элементов из двух списков l1 и l2,
       сохраняющих порядок следования элементов в этих списках:
       l1=[1,2,3] l2=['+','-'] -> [1,2,'+',3,'-']; ['+',1,2,'-',3] и тд
       m - глубина рекурсии = len(l1)+len(l2)
       prefix - возвращаемая перестановка
    """ 
    prefix = prefix or []
    if m == 0:
        yield prefix
    if len(l1) > 0:
        yield from gen_ordered_permutations(l1[1:],l2,m-1,prefix+[l1[0]])
    if len(l2) > 0:
        yield from gen_ordered_permutations(l1,l2[1:],m-1,prefix+[l2[0]])

def gen_groups(data,m,prefix=None):
    """генератор группировок чисел:
       data = '123456' -> [1,2,3,4,5,6], [12,3,4,5,6], [1,234,5,6] и тд
       prefix - возвращаемая группировка
    """
    prefix = prefix or []

    if m == 0:
        yield prefix
    
    for i in range(m):
        if len(data) > i:
            yield from gen_groups(data[i+1:],m-i-1,prefix+[int(data[0:i+1])])

def checkio(data):
    if int(data) == 100:
        return False
    operations = ['+','-','*','/']
    for combination in gen_groups(data,len(data)):
        if len(combination) == 1:
            continue
        for oper_set in itertools.product(operations,repeat=len(combination)-1):
            l1 = combination[2:]
            l2 = list(oper_set)
            for o_perm in gen_ordered_permutations(l1,l2,len(l1)+len(l2)):
                rpn_expression = combination[0:2]+list(o_perm)
                if rpn(rpn_expression) == 100:
                    return False
    return True

def find100(data):
    if int(data) == 100:
        return [100], True
    operations = ['+','-','*','/']
    for combination in gen_groups(data,len(data)):
        if len(combination) == 1:
            continue
        for oper_set in itertools.product(operations,repeat=len(combination)-1):
            l1 = combination[2:]
            l2 = list(oper_set)
            for o_perm in gen_ordered_permutations(l1,l2,len(l1)+len(l2)):
                rpn_expression = combination[0:2]+list(o_perm)
                if rpn(rpn_expression) == 100:
                    return rpn_expression,True    
    return None,False


def test0():    
    tests = ['000100',
             '600500',
             '001010',
             '101000',
             '000100',
             '271353',
             '593347',
             '707409',
             '595347',
             '000000',
             '561709',
             '593347',
             '000955',
             '100478',
             '100479',
             '725126',
             '836403',
             '240668',
             '082140',
             '574699',
             '111111',
             '555555',
             '777777',
             '392039',
             '712922',
             '279216',
             '173403',
             '064027',
             '237867'
             ]

    for i,test in enumerate(tests):
        print(f'test#{i}: {test} {find100(test)} best_clear_check:{not checkio_clear(test)}')

#best clear solution
#отсюда https://py.checkio.org/mission/mathematically-lucky-tickets/publications/tamacjp/python-3/first/?ordering=most_voted&filtering=all
def divide(data):
    # as integer (allow over 10)
    yield int(data)

    # divide 123456: 1 23456, 12 3456, 123 456, ...
    for pos in range(1, len(data)):
        for left in divide(data[:pos]):
            for right in divide(data[pos:]):
                # calculate + - * /
                yield left + right
                yield left - right
                yield left * right
                if right:
                    yield left / right
def checkio_clear(data):
    # enumerate all pattern
    for x in divide(data):
        if x == 100:
            return False
    return True

#These "asserts" using only for self-checking and not necessary for auto-testing
if __name__ == '__main__':
    assert checkio('000000') == True, "All zeros"
    assert checkio('707409') == True, "You can not transform it to 100"
    assert checkio('595347') == False, "(5 + ((9 / (3 / 34)) - 7)) = 100"
    assert checkio('271353') == False, "(2 - (7 * (((1 / 3) - 5) * 3))) = 100"
    test0()
    print('All done!')