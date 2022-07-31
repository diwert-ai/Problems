# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Given a string s, find the length of the longest substring without
# repeating characters.

class Solution:
    # my first solution O(N^3) - time
    @staticmethod
    def length_of_longest_substring(s: str) -> int:
        res = 0
        for i in range(len(s)):
            sub = [s[i]]
            for j in range(i + 1, len(s)):
                if s[j] not in sub:
                    sub.append(s[j])
                else:
                    break
            length = len(sub)
            if length > res:
                res = length

        return res

    # sliding window approach O(N^2) - time
    @staticmethod
    def length_of_longest_substring_sw(s: str) -> int:
        res = 0
        right = 1
        for left in range(len(s)):
            while right < len(s) and s[right] not in s[left:right]:
                right += 1
            res = max(res, right - left)
        return res

    # sliding window + hash table O(N) - time
    # https://leetcode.com/problems/longest-substring-without-repeating-characters/discuss/1731/A-Python-solution-85ms-O(n)
    @staticmethod
    def length_of_longest_substring_swh(s):
        used = {}
        max_length = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)
            used[c] = i
        return max_length


if __name__ == '__main__':
    tests = [('a', 1),
             ('abcabcbb', 3),
             ('bbbbb', 1),
             ('pwwkew', 3)]

    for test, result in tests:
        print(f'{test}\ntrue result: {result}\n' +
              f'my result: {Solution().length_of_longest_substring(test)}\n' +
              f'sw: {Solution().length_of_longest_substring_sw(test)}\n' +
              f'swh: {Solution().length_of_longest_substring_swh(test)}\n')
