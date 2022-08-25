# https://leetcode.com/problems/implement-strstr/
# Implement strStr().
# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview.
# For the purpose of this problem, we will return 0 when needle is an empty string.
# This is consistent to C's strstr() and Java's indexOf().
class Solution:
    # алгоритм KMP (Кнута-Морриса-Пратта)
    @staticmethod
    def prefix_func(s: str):
        n = len(s)
        pi = [0] * n
        for i in range(1, n):
            p = pi[i - 1]
            while s[i] != s[p] and p > 0:
                p = pi[p - 1]
            if s[i] == s[p]:
                p += 1
            pi[i] = p
        return pi

    def str_str(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0
        ls = len(needle)
        p = self.prefix_func(needle + '#' + haystack)
        for i in range(len(p)):
            if p[i] == ls:
                return i - 2 * ls
        return -1


def test0():
    h = 'sdndashjkasdjhaggdggjskasjhd'
    n = 'sdjha'
    print(Solution().str_str(h, n), h.find(n))


if __name__ == '__main__':
    test0()
