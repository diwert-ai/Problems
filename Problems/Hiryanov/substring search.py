# пример: поиск подстроки в строке
# из лекции Хирьянова https://www.youtube.com/watch?v=rEPggzaPoUw&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=12


# проверка равенства двух строк
# O(N) - время, N - длина строки
def equal(a: str, b: str):
    n = len(a)
    if n != len(b):
        return False

    for i in range(n):
        if a[i] != b[i]:
            return False

    return True


# поиск всех подстрок
# наивный метод - перебор. время О ((N-M) * M) где N - длина строки,
# M - длина подстроки
def search_subs(s: str, sub: str):
    n = len(s)
    m = len(sub)
    if n < m:
        return False, -1

    index = []

    for i in range(n-m+1):
        if equal(sub, s[i:i+m]):
            index.append(i)

    return (True, index) if index != [] else (False, -1)

# префикс функция {\pi} строки
# собственный суффикс - суффикс (окончание), не равный самой строке
# префикс функция строки {\pi_s} - длина максимального собственного
# суффикса, который является префиксом.


'''
Быстрое вычисление префикс функции. О(N) по времени.
Пускай известны значения префикс функции {\\pi_{s_i}} для всех срезов строки s[:i]. 
Будем вычислять пи функцию для s[:i+1], т.е. pi[i] (pi[j] для всех j < i нам известны, pi[0]=0)
Добавляем новый символ x к срезу строки s[:i]. Некоторая подстрока s[:i]  является ее префиксом 
и суффиксом - длина этой продстроки возвращает префикс функция {\\pi_{s_i}}. Тогда если следующий за
префиксом символ s[p] (его индекс будет p, где p = {\\pi_{s_i}}=pi[i-1]) совпадает с x, то префикс функция 
расширенного символом x среза s[:i] увеличивается на 1, т.е.
{\\pi_{s_{i+1}}} = {\\pi_{s_i}} + 1 или pi[i] = pi[i-1]+1.  А если символы не совпали, то рассматриваем  значение 
пи функции от префикса, найденного на предыдущем шаге, которое дает нам длину следующего по величение префикса и
суффикса для проверки на совпадение символа идущего за новым префиксом  с добавляемым симвлом  x - и так до тех
пока не встретится совпадение, либо искомое значение будет равна 0.
'''


def prefix_func(s: str):
    n = len(s)
    pi = [0]*n

    for i in range(1, n):
        p = pi[i-1]
        while s[i] != s[p] and p > 0:
            p = pi[p-1]

        if s[i] == s[p]:
            p += 1 
   
        pi[i] = p

    return pi, pi[-1]


# Алгоритм Кнута-Морриса-Пратта (КМП)
def kmp(s: str, sub: str):
    t = sub + '#' + s
    index = []
    ls = len(sub)   
    p, _ = prefix_func(t)

    for i in range(len(p)):
        if p[i] == ls:
            index.append(i-2*ls)
    
    return (False, -1) if index == [] else (True, index)


def test0():
    a = 'assas'
    b = 'assas'
    c = 'asssad'
    d = 'asddsa'

    print(f'{a}=={b} {equal(a,b)} {a==b}')
    print(f'{b}=={c} {equal(b,c)} {b==c}')
    print(f'{c}=={d} {equal(c,d)} {c==d}')
    print()


def test1():
    s = 'nnsmasamsnndsm,asamsn'
    sub = 'amsn'
    print(f'search {sub} in {s}\nnaive search: {search_subs(s,sub)}')
    print()


def test2():
    s = 'abcdabcabcdabcdab'
    print(f'pref_func({s}):\n{prefix_func(s)}')
    print()


def test3():
    s = 'suassdasdaabcsubasubsusuassdasdbsubsuasdasdbsuassdasd'
    sub = 'suassdasd'
    print(f'search {sub} in {s}\nkmp: {kmp(s,sub)}\nnaive search: {search_subs(s,sub)}')
    print()


if __name__ == '__main__':
    test0()
    test1()
    test2()
    test3()
