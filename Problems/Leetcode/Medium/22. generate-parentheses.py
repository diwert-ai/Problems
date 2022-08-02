# https://leetcode.com/problems/generate-parentheses/
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# Time Complexity : O(\dfrac{4^n}{\sqrt{n}}).
# Each valid sequence has at most n steps during the backtracking procedure.
# Space Complexity : O(\dfrac{4^n}{\sqrt{n}}),
# as described above, and using O(n)O(n) space to store the sequence.

class Solution:
    def __init__(self):
        self.max_sum = 0
        self.result = []
        self.op1 = 0
        self.op2 = 0
    
    # мое решение
    def add_variant(self, cur_sum, line):
        if len(line) == 2*self.max_sum:
            if cur_sum == 0:
                self.result.append(line)
            return
        
        self.op1 += 1
        if cur_sum < self.max_sum:
            self.add_variant(cur_sum+1, line+'(')
        
        if cur_sum > 0:
            self.add_variant(cur_sum-1, line+')')
        
        return

    def generate_parenthesis(self, n: int) -> list[str]:
        self.max_sum = n      
        self.add_variant(0, '')
        return self.result

    # более быстрое решение (~ в 4 раза)
    def generate_parenthesis_fast(self, n: int) -> list[str]:
        ans = []

        def backtrack(line=None, left=0, right=0):
            line = line or []
            if len(line) == 2 * n:
                ans.append("".join(line))
                return

            self.op2 += 1
            if left < n:
                line.append("(")
                backtrack(line, left+1, right)
                line.pop()
            if right < left:
                line.append(")")
                backtrack(line, left, right+1)
                line.pop()
        backtrack()
        return ans


def test0():
    print(*Solution().generate_parenthesis(4), sep='\n')
    print('')
    print(*Solution().generate_parenthesis_fast(4), sep='\n')


def test1():
    s = Solution()
    s.generate_parenthesis(5)
    s.generate_parenthesis_fast(5)

    print(s.op1/s.op2)


if __name__ == '__main__':
    test0()
    test1()
