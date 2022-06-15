#https://leetcode.com/problems/valid-parentheses/
#Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
#An input string is valid if:
#
#Open brackets must be closed by the same type of brackets.
#Open brackets must be closed in the correct order.
class Solution:
    def isValid(self, s: str) -> bool:
        st =[]
        for c in s:
            if c in '({[':
                st.append(c)
            else:
                #assert c in ')}]', f"right brace expected: got {c}"

                if len(st) == 0:
                    return False

                left=st.pop()
                if  (c == ')' and left != '(') or \
                    (c == '}' and left != '{') or \
                    (c == ']' and left != '['): 
                    return False


        return len(st) == 0

tests = [('{}', True),('{}{}()((((([[[[]]]])))))', True),('{[}]',False)]
sol = Solution()
for s,r in tests:
    print(sol.isValid(s),r)