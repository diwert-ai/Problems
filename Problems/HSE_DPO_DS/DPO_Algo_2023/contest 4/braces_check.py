# https://contest.yandex.ru/contest/49847/problems/A/
# Рассмотрим последовательность, состоящую из круглых, квадратных и фигурных скобок. Программа должна определить,
# является ли данная скобочная последовательность правильной.
# Пустая последовательность является правильной. Если A – правильная, то последовательности (A), [A], A – правильные.
# Если A и B – правильные последовательности, то последовательность AB – правильная.

def braces_check(string):
    brace_map = {'(': ')', '{': '}', '[': ']'}
    stack = list()
    for brace in string:
        if brace in '({[':
            stack.append(brace)
        else:
            if not stack or brace_map[stack.pop()] != brace:
                return False

    return not stack


def test0():
    brace_seqs = ('()[]{}', '', '()(){[{(())}]}', '((({)[})]))')
    for seq in brace_seqs:
        print(braces_check(seq))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
