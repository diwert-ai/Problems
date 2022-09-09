import re


def tokenize(expression):
    if expression == "":
        return []

    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}

    def input(self, expression):
        tokens = tokenize(expression)
        print(tokens)


variables = {}
operators = ('+', '-', '*', '/', '%')
precedence = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '=': '0'}


def parse_variable(var):
    if var in variables:
        return variables[var]
    print(f"ERROR: Invalid identifier. No variable with name '{var}' was found.")
    return None


def calculate(x, y, operation):
    if operation == '+':
        x += y
    elif operation == '-':
        x -= y
    elif operation == '*':
        x *= y
    elif operation == '/':
        x /= y
    elif operation == '%':
        x %= y
    return x


def rpn(expression: list):
    stack = []
    for token in expression:
        if token in operators:
            y, x = stack.pop(), stack.pop()
            x = parse_variable(x) if type(x) is str else x
            y = parse_variable(y) if type(y) is str else y
            if x is None or y is None:
                return None
            x = calculate(x, y, token)
            stack.append(x)
        elif token == '=':
            y, x = stack.pop(), stack.pop()
            if type(x) is not str:
                print(f'Syntax error! {x} is not variable!')
                return None
            y = parse_variable(y) if type(y) is str else y
            variables[x] = y
            stack.append(y)
        elif type(token) in [int, float, str]:
            stack.append(token)
        else:
            print(f'Unexpected token: {token}')
            return None

    return stack.pop()


def gen_rpn(expression: list):
    """Shunting yard algorithm by Edsger Dijkstra
    https://en.wikipedia.org/wiki/Shunting_yard_algorithm
    """
    out = []
    stack = []
    for token in expression:
        if token in operators:


    return out


def test0():
    print(rpn([10, 'f', 1, 5, '-', '=', '*']))
    print(rpn(['a', 4, '=', 'b', 6, '=']))
    print(rpn([1, 'f', 'b', '*', '-']))
    print(rpn(['var10', 2, '=']))
    print(rpn(['c', 10.1, '=']))
    print(rpn(['d', 15.45, '=']))
    print(rpn(['w', 100, 'a', 'a', '*', 'var10', 'var10', '*', '+', '*', '=']))
    print(rpn(['k', 'c', 'd', '-', '=']))
    print(variables)


def test1():
    interpreter = Interpreter()
    interpreter.input('y = (x + 10.3) * (z + 5)')


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
