def norm_bracket_sequence(line: str):
    stack = []
    for token in line:
        if token in '({[':
            stack.append(token)
        else:
            if len(stack) == 0:
                return False
            left_brace = stack.pop()
            if (token == ')' and left_brace != '(') or \
               (token == '}' and left_brace != '{') or \
               (token == ']' and left_brace != '['):
                return False

    return len(stack) == 0


def remove_brackets(line: str, stack=None, out=''):
    stack = stack or []
    open_bracket = False
    out = out
    for i, token in enumerate(line):
        if token in '({[':
            stack.append(token)
            open_bracket = True
        else:
            if len(stack) == 0:
                continue
            left_brace = stack.pop()
            if (token == ')' and left_brace != '(') or \
               (token == '}' and left_brace != '{') or \
               (token == ']' and left_brace != '['):
                out1 = remove_brackets(line[i:], stack+[], out)
                out2 = remove_brackets(line[i+1:], stack+[left_brace], out)
                if len(out1) > len(out2):
                    out = out1
                else:
                    out = out2
                return out

            if open_bracket:
                out += left_brace + token
            else:
                out = left_brace + out + token

            open_bracket = False

    return out


lines = dict()


def remove_brackets_bf(line: str) -> str:
    if line in lines:
        return lines[line]
    n = len(line)
    if n < 2:
        return ''
    if norm_bracket_sequence(line):
        return line
    out = ''
    for i in range(len(line)):
        next_line = line[:i]+line[i+1:]
        res = remove_brackets_bf(next_line)
        lines[next_line] = res
        if len(res) > len(out):
            out = res
        if len(out) == n - 1:
            return out
    return out


def test0():
    print("Example:")
    print(remove_brackets("(()()"))
    print(remove_brackets("[[(}]]"))
    print(remove_brackets("[(()]"))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert remove_brackets("(()()") == "()()"
    assert remove_brackets("[][[[") == "[]"
    assert remove_brackets("[[(}]]") == "[[]]"
    assert remove_brackets("[[{}()]]") == "[[{}()]]"
    assert remove_brackets("[[[[[[") == ""
    assert remove_brackets("[[[[}") == ""
    assert remove_brackets("") == ""
    assert remove_brackets("[(])") == "()"
    print("Coding complete? Click 'Check' to earn cool rewards!")


def test1():
    print(remove_brackets_bf('[[{}()]]([{])}(]{'))


if __name__ == '__main__':
    test1()
