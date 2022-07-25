#https://leetcode.com/problems/regular-expression-matching/
#Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
#
#'.' Matches any single character.​​​​
#'*' Matches zero or more of the preceding element.
#The matching should cover the entire input string (not partial).

class Solution:
    #наивное решение
    def isMatchF(self, s: str, p: str) -> bool:
        if s == p: 
            return True
        
        if '.' not in p and '*' not in p and s!=p:
            return False
        
        lp = len(p)
        ls = len(s)
        

        c_p = p[lp-1]
        
        if (ls != 0 ):
            c_s = s[ls-1]
        else:
            c_s = ""
        
        if c_p in (c_s,'.'):
            return lp!=0 and ls !=0 and self.isMatch(s[:-1],p[:-1])
        else:
            if c_p == '*':
                cp2 = p[lp-2]               
                return (ls!= 0 and self.isMatch(s[:-1],p) and (c_s==cp2 or cp2=='.')) or self.isMatch(s,p[:-2])   
            else:
                return False

    # короткое рекурсивное  решение
    # ассимптотика по времени: O((T+P)*2^{T+P/2})
    # по памяти: O((T+P)*2^{T+P/2}) (T=len(s), P=len(p)) 
    def isMatch(self, s: str, p: str) -> bool:
        if not p: return not s
        
        f_match = bool(s) and p[0] in [s[0],'.']
        
        if len(p)>=2 and p[1] == '*':
            return self.isMatch(s,p[2:]) or f_match and self.isMatch(s[1:],p)
        else:
            return f_match and self.isMatch(s[1:],p[1:])

    # DP решение с рекурсией
    # время O(T*P) память O(T*P)

    def isMatch_DP(self, text, pattern):
        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                    else:
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)



def test0():
    s = 'ababcdfq'
    p = 'a*b*a*b*...'

    sol = Solution()
    print(sol.isMatch(s,p))
    print(sol.isMatchF(s,p))
    print(sol.isMatch_DP(s,p))

if __name__ == '__main__':
    test0()
