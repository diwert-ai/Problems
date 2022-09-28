# https://www.codewars.com/kata/5985ea20695be6079e000003
from random import choice, choices


# рекурсивный поиск с возвратом - долго по времени (O(n!) ? или даже просто экспонента от n)
def solve_n_queens(n, fixed_queen):
    forbidden_fields = {(i, j): 0 for i in range(n) for j in range(n)}
    queens = {fixed_queen}
    q_cash = set()

    def forbid_cells(row, col):
        nonlocal forbidden_fields
        for i in range(n):
            forbidden_fields[(i, col)] += 1

        for j in range(n):
            forbidden_fields[(row, j)] += 1

        zp1 = zip(range(row - col, n), range(col + n - row)) if row >= col else zip(range(row + n - col),
                                                                                    range(col - row, n))
        for i, j in zp1:
            forbidden_fields[(i, j)] += 1

        zp2 = zip(range(n - 1, col - n + row, -1), range(col - n + row + 1, n)) if col - n + row + 1 >= 0 else zip(
            range(col + row, -1, -1), range(0, col + row + 1))

        for i, j in zp2:
            forbidden_fields[(i, j)] += 1

        forbidden_fields[(row, col)] -= 3

    def unforbid_cells(row, col):
        nonlocal forbidden_fields
        for i in range(n):
            forbidden_fields[(i, col)] -= 1

        for j in range(n):
            forbidden_fields[(row, j)] -= 1

        zp1 = zip(range(row - col, n), range(col + n - row)) if row >= col else zip(range(row + n - col),
                                                                                    range(col - row, n))
        for i, j in zp1:
            forbidden_fields[(i, j)] -= 1

        zp2 = zip(range(n - 1, col - n + row, -1), range(col - n + row + 1, n)) if col - n + row + 1 >= 0 else zip(
            range(col + row, -1, -1), range(0, col + row + 1))

        for i, j in zp2:
            forbidden_fields[(i, j)] -= 1

        forbidden_fields[(row, col)] += 3

    forbid_cells(*fixed_queen)

    def set_queens(number):
        nonlocal queens
        if len(queens) == n:
            return n
        if number:
            row_set = set(range(0, n)) - {queen[0] for queen in queens}
            col_set = set(range(0, n)) - {queen[1] for queen in queens}
            for q_row in row_set:
                for q_col in col_set:
                    if forbidden_fields[(q_row, q_col)] == 0:
                        if frozenset(queens | {(q_row, q_col)}) in q_cash:
                            continue
                        queens.add((q_row, q_col))
                        forbid_cells(q_row, q_col)
                        if set_queens(number - 1) == n:
                            return n
                        else:
                            q_cash.add(frozenset(queens))
                            q_cash.add(frozenset((j, i) for i, j in queens))
                            q_cash.add(frozenset((j, n - i - 1) for i, j in queens))
                            q_cash.add(frozenset((n - i - 1, j) for i, j in queens))
                            q_cash.add(frozenset((n - i - 1, n - j - 1) for i, j in queens))
                            q_cash.add(frozenset((n - j - 1, n - i - 1) for i, j in queens))
                            q_cash.add(frozenset((n - j - 1, i) for i, j in queens))
                            q_cash.add(frozenset((i, n - j - 1) for i, j in queens))
                            queens -= {(q_row, q_col)}
                            unforbid_cells(q_row, q_col)

        return len(queens)

    set_queens(n - 1)
    q_list = [[' Q ' if (i, j) in queens else ' . ' for j in range(n)] for i in range(n)]
    return None if len(queens) < n else '\n'.join((''.join(line) for line in q_list))


# https://en.wikipedia.org/wiki/Eight_queens_puzzle
# Алгоритм генератора корректных расстановок
# (изложен в книге Н. Вирта  "Алгоритмы и структуры данных" - советское издание "Мир 1977 г.")
# https://doc.lagout.org/science/0_Computer%20Science/2_Algorithms/Algorithms%20and%20Data%20Structures%20%28RU%29.pdf
def n_queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i + j not in b and i - j not in c:
                yield from n_queens(n, i + 1, a + [j], b + [i + j], c + [i - j])
    else:
        yield a


def gen_random_permutation(n: int, fixed: tuple):
    fixed_row, fixed_column = fixed
    columns, rows, perm = list(range(n)), list(range(n)), [0] * n
    columns.remove(fixed_column)
    rows.remove(fixed_row)
    perm[fixed_row] = fixed_column
    for row in rows:
        column = choice(columns)
        perm[row] = column
        columns.remove(column)
    return perm


def collision_arrays(position: list):
    n = len(position)
    positive_diagonal = [0] * (2 * n - 1)
    negative_diagonal = [0] * (2 * n - 1)
    for row, column in enumerate(position):
        positive_diagonal[position[row] + row] += 1
        negative_diagonal[position[row] - row + n - 1] += 1
    return positive_diagonal, negative_diagonal
    # return sum((k-1 for k in positive_diagonal+negative_diagonal if k))


# A Polynomial Time Algorithm for the N-Queens Problem
# Rok Sosic and Jun Gu
# (appeared in SIGART Bulletin, Vol. 1, 3, pp. 7-11, Oct, 1990.)
# https://citeseerx.ist.psu.edu/viewdoc/download;jsessionid=4DC9292839FE7B1AFABA1EDB8183242C?doi=10.1.1.57.4685&rep=rep1&type=pdf
# Алгоритм завершения расстановки ферзей методом градиентного спуска.
def solve_n_queens_2(n, fixed_queen):
    rows = list(range(n))
    rows.remove(fixed_queen[0])
    runs = 0
    while runs < 100:
        position = gen_random_permutation(n, fixed_queen)
        pos, neg = collision_arrays(position)
        collision_number = sum((k - 1 for k in pos + neg if k > 1))
        for k, i in enumerate(rows):
            for j in rows[k + 1:]:
                q1 = position[i]
                q2 = position[j]
                if pos[q1 + i] > 1 or pos[q2 + j] > 1 or neg[q1 - i + n - 1] > 1 or neg[q2 - j + n - 1] > 1:
                    d_pos = {q1 + i, q1 + j, q2 + j, q2 + i}
                    d_neg = {q1 - i + n - 1, q1 - j + n - 1, q2 - j + n - 1, q2 - i + n - 1}
                    delta = sum((pos[d] - 1 for d in d_pos if pos[d] > 1)) +\
                        sum((neg[d] - 1 for d in d_neg if neg[d] > 1))
                    pos[q1 + i] -= 1
                    pos[q1 + j] += 1
                    pos[q2 + j] -= 1
                    pos[q2 + i] += 1
                    neg[q1 - i + n - 1] -= 1
                    neg[q1 - j + n - 1] += 1
                    neg[q2 - j + n - 1] -= 1
                    neg[q2 - i + n - 1] += 1
                    new_delta = sum((pos[d] - 1 for d in d_pos if pos[d] > 1)) +\
                        sum((neg[d] - 1 for d in d_neg if neg[d] > 1))
                    if new_delta < delta:
                        position[i], position[j] = position[j], position[i]
                        collision_number = collision_number - delta + new_delta
                    else:
                        pos[q1 + i] += 1
                        pos[q1 + j] -= 1
                        pos[q2 + j] += 1
                        pos[q2 + i] -= 1
                        neg[q1 - i + n - 1] += 1
                        neg[q1 - j + n - 1] -= 1
                        neg[q2 - j + n - 1] += 1
                        neg[q2 - i + n - 1] -= 1
        if collision_number == 0:
            line = '.' * n
            return runs, '\n'.join((line[:column] + 'Q' + line[column + 1:] for column in position)) + '\n'
        runs += 1
    return None


def test0():
    s_row = 0
    s_col = 2
    for solution in n_queens(10, 0, [], [], []):
        if solution[s_row] == s_col:
            print(solution)
            return


def test1():
    print(solve_n_queens(10, (7, 4)))


def test2():
    array = [1, 2, 3, 4, 5]
    n = 4
    for _ in range(10):
        print(f'{n} choices from array {array}: {choices([1, 2, 3, 4, 5], k=n)}')


def test3():
    n = 10
    k = 7
    for i in range(n):
        print(f'({i},{k}) :{gen_random_permutation(n, (i, k))}')


def test4():
    position = [0, 2, 4, 1, 3, 12, 14, 11, 17, 19, 16, 8, 15, 18, 7, 9, 6, 13, 5, 10]
    pos, neg = collision_arrays(position)
    print(f'collision number {position}: {sum((k - 1 for k in pos + neg if k))}')


def test5():
    for n in range(1, 1000, 10):
        r, _ = solve_n_queens_2(n, (n//2, n//2))
        print(n, r)


if __name__ == '__main__':
    test_funcs = [test0, test1, test2, test3, test4, test5]
    for test in test_funcs:
        test()
