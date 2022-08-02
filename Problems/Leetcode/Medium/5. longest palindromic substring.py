# https://leetcode.com/problems/longest-palindromic-substring/
# Given a string s, return the longest palindromic substring in s.

class Solution:
    @staticmethod
    def get_me_more(lst: list, s: str, ls: int) -> list:
        res = []
        for i in lst:
            start = i[0] - 1
            end = i[1] + 1
            if start >= 0 and end < ls:
                if s[start] == s[end]:
                    res.append([start, end])
        return res

    # my solution
    def longest_palindrome(self, s: str) -> str:
        lst = []
        l_prev = [[0, 0]]
        ls = len(s)

        for i in range(ls - 1):
            if s[i] == s[i + 1]:
                lst.append([i, i + 1])

        for i in range(1, ls - 1):
            lst.append([i, i])

        l_cur = lst
        while l_cur:
            l_prev = l_cur
            l_cur = self.get_me_more(l_cur, s, ls)
        
        return s[l_prev[0][0]:l_prev[0][1] + 1]


if __name__ == '__main__':
    tests = [("babad", "bab"),
             ("cbbd", "bb"),
             ("asanmnasl", "sanmnas")]

    for test, right_answer in tests:
        print(f'{test}\nright answer: {right_answer}\n'
              f'my answer: {Solution().longest_palindrome(test)}\n')
