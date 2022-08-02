# https://leetcode.com/problems/valid-parentheses/
# Given a string s containing just the characters '(', ')',
# '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.


class Solution:
    @staticmethod
    def is_valid(s: str) -> bool:
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            else:
                assert c in ')}]', f"right brace expected: got {c}"

                if len(stack) == 0:
                    return False

                left = stack.pop()
                if (c == ')' and left != '(') or \
                   (c == '}' and left != '{') or \
                   (c == ']' and left != '['):
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    tests = [('{}', True),
             ('{}{}()((((([[[[]]]])))))', True),
             ('{[}]', False),
             ('({)[({]})}', False)]
    for test_s, test_r in tests:
        print(Solution.is_valid(test_s), test_r)
