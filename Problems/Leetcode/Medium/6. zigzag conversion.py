# https://leetcode.com/problems/zigzag-conversion/
# The string "PAYPALISHIRING" is written in a zigzag
# pattern on a given number of rows like this:
# (you may want to display this pattern in a fixed font for better legibility)

# P   A   H   N
# A P L S I I G
# Y   I   R

class Solution:
    lst = []

    def zig(self, s, start, num_rows):
        for i in range(num_rows):
            cur = start + i
            if cur == len(s):
                return 0
            self.lst[i].append(s[cur])
        return start + num_rows

    def zag(self, s, start, num_rows):
        for i in range(num_rows - 2, 0, -1):
            cur = start + num_rows - i - 2
            if cur == len(s):
                return 0
            self.lst[i].append(s[cur])
        return start + num_rows - 2

    # мое решение
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1:
            return s

        self.lst = [[] for _ in range(num_rows)]
        start = 0
        while True:
            start = self.zig(s, start, num_rows)
            if start == 0:
                break
            start = self.zag(s, start, num_rows)
            if start == 0:
                break

        res = ''
        for i in range(num_rows):
            res += ''.join(self.lst[i])

        return res


if __name__ == '__main__':
    tests = [("PAYPALISHIRING", 3),
             ("PAYPALISHIRING", 4),
             ("A", 1)]

    for test, test_num_rows in tests:
        print(f'zigzag for {test}: {Solution().convert(test, test_num_rows)}')

