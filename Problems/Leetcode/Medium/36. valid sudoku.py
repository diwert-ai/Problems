# https://leetcode.com/problems/valid-sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need
# to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note:
# A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
from typing import List
from collections import Counter


# my solution
class Solution:
    @staticmethod
    def is_valid_sudoku(board: List[List[str]]) -> bool:
        valid_values = list(str(x) for x in range(10))
        for row in board:
            if not all(x in valid_values and row.count(x) == 1 for x in row if x != '.'):
                return False

        columns = [[row[i] for row in board] for i in range(9)]
        for column in columns:
            if not all(x in valid_values and column.count(x) == 1 for x in column if x != '.'):
                return False

        blocks = [[board[i+3*k][j+3*m] for i in range(3) for j in range(3)] for k in range(3) for m in range(3)]
        for block in blocks:
            if not all(x in valid_values and block.count(x) == 1 for x in block if x != '.'):
                return False

        return True

    # solutions by Stefan Pochmann
    # https://leetcode.com/problems/valid-sudoku/discuss/15460/1-7-lines-Python-4-solutions
    @staticmethod
    def is_valid_sudoku_sp1(board):
        return 1 == max(Counter(
            x
            for i, row in enumerate(board)
            for j, c in enumerate(row)
            if c != '.'
            for x in ((c, i), (j, c), (i/3, j/3, c))
        ).values())

    @staticmethod
    def is_valid_sudoku_sp2(board):
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i, row in enumerate(board)
                    for j, c in enumerate(row)
                    if c != '.'), [])
        return len(seen) == len(set(seen))

    @staticmethod
    def is_valid_sudoku_sp3(board):
        seen = set()
        return not any(x in seen or seen.add(x)
                       for i, row in enumerate(board)
                       for j, c in enumerate(row)
                       if c != '.'
                       for x in ((c, i), (j, c), (i / 3, j / 3, c)))

    @staticmethod
    def is_valid_sudoku_sp4(board):
        seen = sum(([(c, i), (j, c), (i / 3, j / 3, c)]
                    for i in range(9) for j in range(9)
                    for c in [board[i][j]] if c != '.'), [])
        return len(seen) == len(set(seen))


def test0():
    boards = [[["5", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]],
              [["8", "3", ".", ".", "7", ".", ".", ".", "."],
               ["6", ".", ".", "1", "9", "5", ".", ".", "."],
               [".", "9", "8", ".", ".", ".", ".", "6", "."],
               ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
               ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
               ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
               [".", "6", ".", ".", ".", ".", "2", "8", "."],
               [".", ".", ".", "4", "1", "9", ".", ".", "5"],
               [".", ".", ".", ".", "8", ".", ".", "7", "9"]]]

    for board in boards:
        print(Solution.is_valid_sudoku(board),
              Solution.is_valid_sudoku_sp1(board),
              Solution.is_valid_sudoku_sp2(board),
              Solution.is_valid_sudoku_sp3(board),
              Solution.is_valid_sudoku_sp4(board))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
