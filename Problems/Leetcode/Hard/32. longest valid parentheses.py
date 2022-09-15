# https://leetcode.com/problems/longest-valid-parentheses/
# Given a string containing just the characters '(' and ')',
# find the length of the longest valid (well-formed) parentheses substring.

class Solution:
    # my first solution - got too much time
    # almost brute force approach
    @staticmethod
    def longest_valid_parentheses_bf(s: str) -> int:
        ix = []
        ix_s = [(c, i) for i, c in enumerate(s)]

        def pair_by_pair(indexed_list: list):
            len_ix = len(ix) - 1
            while len(ix) > len_ix:
                len_ix, i = len(ix), 0
                while i < len(indexed_list):
                    while i in ix:
                        i += 1
                    j = i + 1
                    while j in ix:
                        j += 1
                    if j < len(indexed_list) and indexed_list[i][0]+indexed_list[j][0] == '()':
                        ix.append(indexed_list[i][1])
                        ix.append(indexed_list[j][1])
                    i = j
                print(len(ix))

        pair_by_pair(ix_s)
        ix.sort()
        result, res = 1, []
        for i in range(1, len(ix)):
            if ix[i] - ix[i-1] == 1:
                result += 1
            else:
                res.append(result)
                result = 1
        res.append(result)
        max_res = max(res)
        return max_res if max_res > 1 else 0

    # second wrong (sic!!!) solution
    @staticmethod
    def p_calc_sum(string: str):
        p_sum = 0
        start = end = 0
        while start < len(string) and string[start] == ')':
            start += 1

        k = 0
        while start + k < len(string) and string[start+k] == '(':
            k += 1
            p_sum += 1

        for i in range(start+k, len(string)):
            p_sum = p_sum + 1 if string[i] == '(' else p_sum - 1
            if p_sum == 0:
                end = i
            if p_sum < 0:
                return start, end, -1, k

        return start, end, p_sum, k

    @staticmethod
    def longest_valid_parentheses(string: str):
        result = []
        i = len(string) - 1
        while i > -1:
            if string[i] == '(':
                i -= 1
            else:
                break
        string = string[:i+1]
        i = 0
        while i < len(string):
            start, end, p_sum, k = Solution.p_calc_sum(string[i:])
            delta = end - start + 1
            result.append(delta) if delta > 1 else None
            if p_sum:
                i = i + end + 1 if p_sum == -1 else (i + start + p_sum - k if p_sum - k > 1 else i + start + 1)
            else:
                break

        return max(result) if result else 0

    # Правильное решение.
    # https://leetcode.com/problems/longest-valid-parentheses/discuss/14312/My-ten-lines-python-solution
    # Суть алгоритма (динамическое программирование). Пусть s входная строка. Пусть f(i) - длина самой длинной
    # подпоследовательности, которая заканчивается на элементе с номером i-1 (нумерация ведется с 0). Инициализируем
    # f(i) нулями для всех i от 0 до n + 1, где n длина строки s. Перебираем элементы s. Если i-й элемент - это
    # открывающая скобка '(', то помещаем ее номер i в стек. Иначе, т.е. i-й элемент закрывающая скобка ')' и при этом
    # стек не пуст, то забираем со стека номер p открывающей скобки и вычисляем f(i+1) = f(p) + (i + 1 - p), т.е. в
    # этом случае длина самой длинной подпоследовательности с концом в i-й скобке ')' есть длина самой длинной
    # подпоследовательности с концом в элементе с номером p-1 плюс расстояние от p элемента до i-го (i + 1 - p).
    # Таким образом верный ответ есть max(f(x)). Сложность и по времени и по памяти O(n), где n число элементов в s.
    @staticmethod
    def longest_valid_parentheses_dp(s):
        dp, stack = [0]*(len(s)+1), []
        for i, c in enumerate(s):
            if c == '(':
                stack.append(i)
            elif stack:
                p = stack.pop()
                dp[i+1] = dp[p] + i - p + 1
        return max(dp)


def test0():
    s = "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((" \
        "(((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((((()())))(())()())((((()())((())))((()))()(" \
        "))))()(()()()(()((()))()()()))()()()(()()((((())()(((()(((())((()))()((()(()))()())))))))))())()())(()()))((" \
        "()()()()())))((()()((((()()))))(())())()()))))(())()(()))((((((()))(()()()()(())(()((()))(()(())(((()()))((" \
        ")((((()((((()((((())(())))()(())))()))(()((((((((())()()((())((()())()))))())())()(((((()()(((((())()((()(((" \
        "()))(()(()))(()(()())))())(()((((()((()(((((()()))((()(()((())()))))(()(()())((()((()((((())))(()())()))()(" \
        "))())()))))(())))(())()((())(()(()))))()())(((()(()(((((((((()(()()())))((()((()())())())(((((()(()))))()))(" \
        ")))))()())()(()(())))(()))))(()))(((()))))())))))(((())((())((((()((()))((())))()))(((()))())()))()()()((()(" \
        ")(()())(()))()()((()())))))())(()())(((())))))())(())()))()())())(()(()((())((()(()((())(()()()(()((()(((()(" \
        "())()(((())))))()())))))(()((((()(()()))(((())(()))(()()))))(())()((()))()))()()))()((())(()())())())(()))((" \
        ")()(())()(()((((()())(((())(()()())())(()()))())))(()((())(()()))))(()))((()()((((()())(()()))()())()())))(" \
        ")(()((((())())()(())()))()()(()(()))))))(((()()((()))(()((((()()((())))())())))()())))())))((())()()()))()((" \
        "()((()))()()())))(())())(()(()(()(()))())()))(())((())()())(((()()(((())(()()))(()())(())))()))(((()()()(" \
        "))))())))(((()))())())())))(((()))()())())())))))()()()()(())))(()())))(()()())))()((((()()()((((()))()(" \
        "))))(()))()))))(()())()))(((((())()((())()))(()())()()()())()(((()(()(())))))(()(((()()))((((()()))()))((((" \
        "))(()(()))()(())))()()(()))))()))))()())))()))((((((((()()())((()(()()()(((())())())))()()(())(())))()())()(" \
        "))))((()))((((())()()))(())(((())(()()(((((()()((()()(((()(()()(((())()))))()(()())(()((((()()())(((()))((" \
        "))((())()))))())))))(()()()())))()))(())((()())()())()()))(())))((()))()()((()())()()))(()()(())()())(())))(" \
        "(()(((())))()))))((((()))((())())())()(())(()))((((((())()()(((((()))()())(((()(()(())()((()())))(((())(()((" \
        "))))))(()(()(((()))(())((((())))((())((((((((()(((((()(())))((((((())(()((((()(())()()((())())())(((((((((" \
        ")))))(((())()))()()))(())(())()()())(()()((())(()))())(((())(()((())(())(())))))(()(()(()()(((()()()))())((" \
        ")))(())())()(((()((())((()())()(((((()()(()))))(((())()()))(()(()(()(()((())))))))(())())()))()(()(()))))()(" \
        ")((((())()())(((())(()))((()())(()((())()()(())((((())))))(())())())(())(()()(()()))(((()((((())(((())))))((" \
        ")()()()(((()((((())(()))((())()))()(((((((()(()())))((()()(()()((())()))()(())))((()()((((()()()))((())()))(" \
        "(())(((()(()()()(((()((())((())()())())))((()))))))))))(())()()(((()()())))(((()))(()))))(((()(()())(()))((" \
        "))((()))(((()(()()(((((((()())((((()))((((()(()())())()(((()(()((()))))))))))()()(((()()((((((((((())))))(((" \
        "(())())((()(((()())()))()()(((((())(()())())(((()((())((((((())(((())(((()(()(((((((()(())()())(()))))(()(((" \
        "()))))))()))(((())))(()(()())()))(()()(()(()((()())()(())((()()((()()()(()(()()))(((((())()(()())()((()())(" \
        ")))(((((()((())()((()((((()(((())())(()()(())()(())(()(())))))(()())((()((()()()())(()))(()))))))(()((())((" \
        "))((())()())()()))(()((()))(()()))()())(())(()()(()))((())()((())((((((())()(()()(((((())(()())())())()()((" \
        ")())))))()))()((())((((((()())((()))))))((()(()()(((((((())))))))((()))(())(((()(()(())()()()()(()(())(" \
        ")))))))())()))()(((((()(())(((()))((()))()))()()(()(()((())(()))))()())((()())))))))(()()(()()))()((()(())(" \
        ")((())(()()))())((()())())()()))))((((()()()))())(())()())))()))()))))()))((()(()())()))()))(((()()()()(" \
        "))))())()))((()()())((()())))(((()((()()())(())))()(())(()(()(())(()(((((()()()(((())()())(()((()())(()((((" \
        ")(())((((()())()(())))(((((((()))))())())))(()))()()(((()())(()))()())(())()))()((())()((())((()((())()())((" \
        ")()))(((((()()()((((((((()(()((()()((((((()())))((((((())))())(()(()((((()(()())())()()))()((())())(()(((((" \
        ")(((()())((())))))(()())(()()()(()))()())()()))((()((()())(())()()()((())()()))))())()))())))(()))(()))()))(" \
        "(())()((()((()))))))())(((()))))))()(((()((())))((()())())()))((()(()(()(()))((()()))())))(()())))())(()))((" \
        "))(())))))()(())(()()))()))((())))(()))(()))))(())()())(()(()))())(()(())(())))(()))())(()())))())(()())(((" \
        ")))()()((()(()()()(((((()((()((())(()())(())))()))))))(((())())))()((((()))()((()))())()))()))(()(()((()()(" \
        "))()()(((()))())))))()((((()()))))()))())))()())))(((((()(())))())(((()))((()))(((()(())())()((()(((()))()(" \
        "))))))((((()))()(()((((((()(()()()())(())((()))()(()()))))))()(((())))(())()())))))((()))(())()))))(()(((()(" \
        ")((())(()))))(((((()))))())))()(())(()(()))()))()))(()((())(()((()())()(((()))))())(())()(())))((())(()((((" \
        ")))(((((()))(()))())))(()((((((())()((((())())()))((())))))())(()(())())))))()()(((())()())))))()))()())))(" \
        ")(())())(())()()()(((())))(())(((()))(()(((()()))())((()))(((()()()()())()()))(()))))()()))))(((()()))))()(" \
        ")(()()))()()()())())()((())(((()())(((())(()((()(((()(()())()()()(()((())(()()(()()()))))))()((()))))()((" \
        ")))()))(())()()())))()()(((()))((()()(((()())))((()()())((())))))()())()((())))())(()())()()()()((())((()()(" \
        "))((()()))())(())())()(()(((()))())(()))))(()()))(())))))))()())()((()())()()))()())))((()()(()())()(()))(((" \
        "))()))(((())))())))(((()()())())("
    print(f'string: {Solution.longest_valid_parentheses(s)} {Solution.longest_valid_parentheses_dp(s)}')


def test1():
    strings = ['((()()(()((()', ')(((((()())()()))()(()))(', '(())(',
               ')))))()()())))))())((', '(((', ')))(((', '((()())))))',
               '()())()()', '((()))', '((((()', '(((()()())))(()()())))']
    for s in strings:
        print(f'{s}: {Solution.longest_valid_parentheses(s)} {Solution.longest_valid_parentheses_dp(s)}')


def test2():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1, test2]
    for test in test_funcs:
        test()