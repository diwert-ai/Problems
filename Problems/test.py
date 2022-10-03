from typing import List


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
        print(Solution.is_valid_sudoku(board))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
