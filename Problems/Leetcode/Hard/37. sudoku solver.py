# https://leetcode.com/problems/sudoku-solver/
# Write a program to solve a Sudoku puzzle by filling the empty cells.
#
# A sudoku solution must satisfy all the following rules:
#
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.

# my solution
class SolutionMy:
    def __init__(self):
        self.solution_variants = dict()
        self.board_values = []
        self.board = None

    def init_solution(self, board):
        self.board = board
        for i, row in enumerate(self.board):
            for j, ij_cell in enumerate(row):
                if ij_cell == '.':
                    self.solution_variants[(i, j)] = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def update_solution_variants(self, i_row, j_column):
        result = self.solution_variants[(i_row, j_column)]
        ij_values = [v for v in self.board_values if len(v) == 2 and (v[0] == j_column or v[1] == i_row)] + \
                    [v for v in self.board_values if len(v) == 3 and v[0] == i_row // 3 and v[1] == j_column // 3]

        for value in ij_values:
            if value[0] in result:
                result.remove(value[0])
            elif value[1] in result:
                result.remove(value[1])
            elif len(value) == 3 and value[2] in result:
                result.remove(value[2])

        self.solution_variants[(i_row, j_column)] = result

    def update_all(self):
        find_new_board_value = False
        self.board_values = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
                                 for i, r in enumerate(self.board)
                                 for j, c in enumerate(r)
                                 if c != '.'), [])
        for i, j in self.solution_variants:
            self.update_solution_variants(i, j)

        for ij in self.solution_variants.copy():
            if len(self.solution_variants[ij]) == 1:
                i, j = ij
                self.board[i][j] = self.solution_variants[ij][0]
                del self.solution_variants[ij]
                find_new_board_value = True
                if not self.is_valid_sudoku():
                    return False
        return find_new_board_value

    def is_valid_sudoku(self):
        seen = sum(([(c, i), (j, c), (i // 3, j // 3, c)]
                    for i, row in enumerate(self.board)
                    for j, c in enumerate(row)
                    if c != '.'), [])

        return len(seen) == len(set(seen))

    def solve_sudoku(self, board):
        self.init_solution(board)

        def backtracking_search():
            while self.update_all():
                pass

            if not self.is_valid_sudoku():
                return False
            else:
                if not self.solution_variants:
                    return True

            sol_variants_copy = {ij: self.solution_variants[ij].copy() for ij in self.solution_variants}
            for i, j in sol_variants_copy:
                for variant in sol_variants_copy[(i, j)]:
                    self.board[i][j] = variant
                    del self.solution_variants[(i, j)]
                    if not backtracking_search():
                        self.solution_variants = dict()
                        for k, l in sol_variants_copy:
                            self.board[k][l] = '.'
                            self.solution_variants[(k, l)] = sol_variants_copy[(k, l)].copy()
                    else:
                        return True
            return False

        backtracking_search()
        for ii in range(9):
            for jj in range(9):
                board[ii][jj] = self.board[ii][jj]

    def print_sudoku(self):
        for row in self.board:
            print(*row)
        print()


# https://leetcode.com/problems/sudoku-solver/discuss/15959/Accepted-Python-solution
# most rated python solution
class SolutionMostRated:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def __init__(self):
        self.board = None

    def solve_sudoku(self, board):
        self.board = board
        self.solve()

    def find_unassigned(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    return row, col
        return -1, -1

    def solve(self):
        row, col = self.find_unassigned()
        # no unassigned position is found, puzzle solved
        if row == -1 and col == -1:
            return True
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if self.is_safe(row, col, num):
                self.board[row][col] = num
                if self.solve():
                    return True
                self.board[row][col] = "."
        return False

    def is_safe(self, row, col, ch):
        box_row = row - row % 3
        box_col = col - col % 3
        if self.check_row(row, ch) and self.check_col(col, ch) and self.check_square(box_row, box_col, ch):
            return True
        return False

    def check_row(self, row, ch):
        for col in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def check_col(self, col, ch):
        for row in range(9):
            if self.board[row][col] == ch:
                return False
        return True

    def check_square(self, row, col, ch):
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == ch:
                    return False
        return True

    def print_sudoku(self):
        for row in self.board:
            print(*row)
        print()


# my variation of most rated python solution above
class SolutionVariation:
    def __init__(self):
        self.board = None

    def solve_sudoku(self, board):
        self.board = board
        self.solve()

    def find_dot_cell(self):
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == '.':
                    return i, j
        return -1, -1

    def is_valid_var(self, row, col, var):
        for c in range(9):
            if self.board[row][c] == var:
                return False

        for r in range(9):
            if self.board[r][col] == var:
                return False

        sr, sc = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[sr+i][sc+j] == var:
                    return False
        return True

    def solve(self):
        row, col = self.find_dot_cell()
        if (row, col) == (-1, -1):
            return True

        variants = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        for variant in variants:
            if self.is_valid_var(row, col, variant):
                self.board[row][col] = variant
                if self.solve():
                    return True
                self.board[row][col] = '.'
        return False

    def print_sudoku(self):
        for row in self.board:
            print(*row)
        print()


def test0():
    boards = [[["5", ".", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
              [[".", "3", ".", "8", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", ".", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", ".", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", ".", ".", ".", "7", "9"]],
              [[".", ".", "9", "7", "4", "8", ".", ".", "."],
               ["7", ".", ".", ".", ".", ".", ".", ".", "."],
               [".", "2", ".", "1", ".", "9", ".", ".", "."],
               [".", ".", "7", ".", ".", ".", "2", "4", "."],
               [".", "6", "4", ".", "1", ".", "5", "9", "."],
               [".", "9", "8", ".", ".", ".", "3", ".", "."],
               [".", ".", ".", "8", ".", "3", ".", "2", "."],
               [".", ".", ".", ".", ".", ".", ".", ".", "6"],
               [".", ".", ".", "2", "7", "5", "9", ".", "."]],
              [[".", ".", ".", "2", ".", ".", ".", "6", "3"],
               ["3", ".", ".", ".", ".", "5", "4", ".", "1"],
               [".", ".", "1", ".", ".", "3", "9", "8", "."],
               [".", ".", ".", ".", ".", ".", ".", "9", "."],
               [".", ".", ".", "5", "3", "8", ".", ".", "."],
               [".", "3", ".", ".", ".", ".", ".", ".", "."],
               [".", "2", "6", "3", ".", ".", "5", ".", "."],
               ["5", ".", "3", "7", ".", ".", ".", ".", "8"],
               ["4", "7", ".", ".", ".", "1", ".", ".", "."]]]

    solutions = [SolutionMy(), SolutionMostRated(),  SolutionVariation()]
    for solution in solutions:
        print(solution.__class__)
        for board in boards:
            solution.solve_sudoku(board)
            solution.print_sudoku()


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
