# https://www.codewars.com/kata/53005a7b26d12be55c000243
import re


def is_float(s):
    """ Returns True is string is a float. """
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_int(s):
    """ Returns True is string is int. """
    try:
        int(s)
        return True
    except ValueError:
        return False


def tokenize(expression):
    if expression == "":
        return []
    regex = re.compile("\s*(=>|[-+*\/\%=\(\)]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
    tokens = regex.findall(expression)
    return [s for s in tokens if not s.isspace()]


class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def peak(self):
        size = len(self.stack)
        return self.stack[size - 1] if size else None


class Interpreter:
    def __init__(self):
        self.vars = {}
        self.functions = {}
        self.operators = ('+', '-', '*', '/', '%')
        self.precedence = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '=': 0}

    def input(self, expression):
        tokens = tokenize(expression)
        rpn_expr = self.gen_rpn(tokens)
        return self.eval_rpn(rpn_expr)

    def parse_variable(self, var):
        if var in self.vars:
            return self.vars[var]
        print(f"ERROR: Invalid identifier. No variable with name '{var}' was found.")
        return None

    @staticmethod
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

    def eval_rpn(self, expression: list):
        if not expression:
            return ''
        stack = MyStack()
        for token in expression:
            if token in self.operators:
                y, x = stack.pop(), stack.pop()
                x = self.parse_variable(x) if type(x) is str else x
                y = self.parse_variable(y) if type(y) is str else y
                if x is None or y is None:
                    print(f'Syntax error!')
                    raise ValueError
                x = self.calculate(x, y, token)
                stack.push(x)
            elif token == '=':
                y, x = stack.pop(), stack.pop()
                if type(x) is not str:
                    print(f'Syntax error! {x} is not variable!')
                    raise ValueError
                y = self.parse_variable(y) if type(y) is str else y
                self.vars[x] = y
                stack.push(y)
            elif type(token) in [int, float, str]:
                stack.push(token)
            else:
                print(f'Unexpected token: {token}')
                raise ValueError
        result = stack.pop()
        if type(result) is str:
            result = self.parse_variable(result)
        if result is None or not stack.is_empty():
            print(f"Syntax error! Result '{result}' is undefined or stack {stack.stack} is not empty!")
            raise ValueError
        return result

    def gen_rpn(self, expression: list):
        """Shunting yard algorithm by Edsger Dijkstra
        https://en.wikipedia.org/wiki/Shunting_yard_algorithm
        """
        out = []
        stack = MyStack()
        for token in expression:
            if token in self.operators or token == '=':
                while (op := stack.peak()) is not None and op in self.operators:
                    if self.precedence[op] >= self.precedence[token]:
                        out.append(stack.pop())
                    else:
                        break
                stack.push(token)
            elif token == '(':
                stack.push(token)
            elif token == ')':
                while stack.peak() != '(':
                    out.append(stack.pop())
                    if stack.is_empty():
                        print("Syntax error! No left parenthesis '(' was found!")
                        raise ValueError
                stack.pop()
            else:
                if is_int(token):
                    out.append(int(token))
                elif is_float(token):
                    out.append(float(token))
                else:
                    out.append(token)
        while not stack.is_empty():
            out.append(stack.pop())

        return out


def test0():
    pass


def test1():
    interpreter = Interpreter()
    while True:
        print(interpreter.input(input()))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
