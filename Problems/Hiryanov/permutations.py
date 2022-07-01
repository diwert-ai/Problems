#пример 'генерация перестановок'
#из лекции Хирьянова https://www.youtube.com/watch?v=2XFaK3bgT7w&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=8


def gen_numbers(n:int,m:int,prefix=[]):
    '''функция генерируящая все N ричные числа занимающие m позиций  от 00...0 до N-1N-1...N-1'''
    if m == 0:
        print(*prefix,sep='')
        return

    for c in range(n):
        prefix.append(c)
        gen_numbers(n,m-1,prefix)
        prefix.pop()

def gen_permutations(n:int,m:int,prefix=[]):
    '''функция генерируящая все перестановки длины n - модификация gen_numbers'''
    if m == 0:
        print(*prefix,sep='')
        return

    for c in [c for c in range(n) if c not in prefix]:
        prefix.append(c)
        gen_permutations(n,m-1,prefix)
        prefix.pop()

if __name__ == '__main__':
    n = 4
    gen_permutations(n,n)


