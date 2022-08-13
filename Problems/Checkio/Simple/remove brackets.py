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


lines = dict()


def remove_brackets(line: str) -> str:
    if line in lines:
        return lines[line]
    n = len(line)
    if n < 2:
        return ''
    if norm_bracket_sequence(line):
        return line
    final_result = ''
    for i in range(len(line)):
        next_line = line[:i]+line[i+1:]
        result = remove_brackets(next_line)
        lines[next_line] = result
        if len(result) > len(final_result):
            final_result = result
        if len(final_result) == n - 1:
            return final_result
    return final_result


if __name__ == "__main__":
    print("Example:")
    print(remove_brackets("(()()"))

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
