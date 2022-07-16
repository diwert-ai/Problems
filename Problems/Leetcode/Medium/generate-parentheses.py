#https://leetcode.com/problems/generate-parentheses/
#Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

#Time Complexity : O(\dfrac{4^n}{\sqrt{n}}). Each valid sequence has at most n steps during the backtracking procedure.
#Space Complexity : O(\dfrac{4^n}{\sqrt{n}}), as described above, and using O(n)O(n) space to store the sequence.

class Solution:
    def __init__(self):
        self.max_sum=0
        self.result=[]
        self.op1 = 0
        self.op2 = 0
    
    #мое решение   
    def add_variant(self,cur_sum,l):
        if len(l) == 2*self.max_sum:
            if cur_sum == 0:
                self.result.append(l)
            return
        
        self.op1 += 1
        if cur_sum < self.max_sum:
            self.add_variant(cur_sum+1,l+'(')
        
        if cur_sum > 0:
            self.add_variant(cur_sum-1,l+')')
        
        return
        
            
    def generateParenthesis(self, n: int) -> list[str]:
        self.max_sum = n      
        self.add_variant(0,'')      
        return self.result

    #более быстрое решение (~ в 4 раза)
    def generateParenthesis2(self, n: int) -> list[str]:
        ans = []
        def backtrack(S = [], left = 0, right = 0):
            if len(S) == 2 * n:
                ans.append("".join(S))
                return
            
            self.op2 += 1
            if left < n:
                S.append("(")
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop()
        backtrack()
        return ans


def test0():
    print(*Solution().generateParenthesis(4), sep='\n')

def test1():
    s = Solution()
    s.generateParenthesis(5)
    s.generateParenthesis2(5)

    print(s.op1/s.op2)

if __name__ == '__main__':
    test0()
    test1()