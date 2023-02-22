from itertools import product


def merge(a, b):
    la, lb, i, j, k = len(a), len(b), 0, 0, 0
    r = [0] * (la + lb)

    while i < la and j < lb:
        if a[i] < b[j]:
            r[k] = a[i]
            i += 1
        else:
            r[k] = b[j]
            j += 1
        k += 1

    if i < la:
        r[k:] = a[i:]
    elif j < lb:
        r[k:] = b[j:]

    return r


def levenstein(a, b):
    n, m = len(a) + 1, len(b) + 1
    f = [[i + j if i == 0 or j == 0 else 0 for j in range(m)] for i in range(n)]
    for i in range(1, n):
        for j in range(1, m):
            if a[i - 1] == b[j - 1]:
                f[i][j] = f[i - 1][j - 1]
            else:
                f[i][j] = 1 + min(f[i - 1][j - 1], f[i - 1][j], f[i][j - 1])

    return f[-1][-1]


def braces_check(string):
    stack = []
    for char in string:
        if char not in '{[()]}':
            continue

        if char in '({[':
            stack.append(char)
        else:
            assert char in ')}]', f"right brace expected: got {char}"

            if not stack:
                return False

            left = stack.pop()
            if (char == ')' and left != '(') or \
                    (char == '}' and left != '{') or \
                    (char == ']' and left != '['):
                return False

    return not stack


roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}


def roman_to_int(s):
    result = 0
    list_s = list(s)
    n = len(list_s)
    for i in range(n - 1):
        d_i = roman[list_s[i]]
        if d_i >= roman[list_s[i + 1]]:
            result += d_i
        else:
            result -= d_i
    result += roman[list_s[n - 1]]
    return result


mapping = {'2': "abc",
           '3': "def",
           '4': "ghi",
           '5': "jkl",
           '6': "mno",
           '7': "pqrs",
           '8': "tuv",
           '9': "wxyz"}


def product2(*args):
    # product2('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


def letter_combinations(digits):
    if not digits:
        return []
    return list(map(''.join, product(*tuple(map(lambda x: mapping[x], digits)))))


def test0():
    pairs = (('horse', 'rorse'),
             ('bug', 'bag'),
             ('hug', 'hat'),
             ('cat', 'bug'),
             ('mud', 'moody'))

    for word1, word2 in pairs:
        print(f'{word1} {word2} {levenstein(word1, word2)}')
    pass


def test1():
    arrays = (([1, 2, 2, 4], [1, 1, 1, 1]),
              ([], []),
              ([], [1, 2, 4, 7, 9]),
              ([1, 1, 1], []),
              ([1, 2, 3, 4, 4, 4, 4, 4, 5], [4, 4, 6, 6, 7, 7]))
    for a, b in arrays:
        print(merge(a, b))


def test2():
    seqs = ('{}([])', '(())[{]}', '[({)]')
    for seq in seqs:
        print(f'seq: {seq} {braces_check(seq)}')


def test3():
    from scipy.stats import binom
    print(binom.pmf(k=5100, n=10000, p=0.5))


def test4():
    tests = ('23', '523', '44', '4327')
    for digits in tests:
        print(letter_combinations(digits))


def test5():
    student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)
    name_surname, birth_year, scores, _ = student
    name, surname = name_surname.split()
    age = 2020 - birth_year
    average_scores = sum(scores) / len(scores)
    increased_scholarship = True if average_scores >= 8 else False

    print(f'Студент: {name}, {surname}')
    print(f'Возраст студента: {age}')
    print(f'Оценки студента: {scores}')
    print(f'Средний балл студента: {average_scores}')
    print(f'Повышенная стипендия: {increased_scholarship}')


if __name__ == '__main__':
    test_funcs = (test0, test1, test2, test3, test4, test5)
    for test in test_funcs:
        test()
