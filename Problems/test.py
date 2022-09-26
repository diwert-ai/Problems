﻿def solve_n_queens(n, fixed_queen):
    forbidden_fields = {(i, j): 0 for i in range(n) for j in range(n)}
    queens = set([fixed_queen])
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


def n_queens(n, i, a, b, c):
    if i < n:
        for j in range(n):
            if j not in a and i+j not in b and i-j not in c:
                yield from n_queens(n, i+1, a+[j], b+[i+j], c+[i-j])
    else:
        yield a


def test0():
    s_row = 2
    s_col = 0
    for solution in queens(8, 0, [], [], []):
        if solution[s_row] == s_col:
            print(solution)
            return


def test1():
    print(solve_n_queens(5, (2, 0)))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
