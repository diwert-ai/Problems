﻿# https://www.codewars.com/kata/53005a7b26d12be55c000243
# https://www.codewars.com/kata/52a78825cdfc2cfc87000005  support unary minus and plus

import re


def is_float(s: str) -> bool:
    """ Returns True if string is float. """
    try:
        float(s)
        return True
    except ValueError:
        return False


def is_int(s: str) -> bool:
    """ Returns True is string is int. """
    try:
        int(s)
        return True
    except ValueError:
        return False


def tokenize(expression: str) -> list:
    if expression == "":
        return []
    regex = re.compile(r"\s*(=>|[-+*/%=()]|[A-Za-z_][A-Za-z0-9_]*|[0-9]*\.?[0-9]+)\s*")
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
        self.args = {}
        self.binary_operators = ('+', '-', '*', '/', '%')
        self.operators = ('+', '-', '*', '/', '%', '~')
        self.precedence = {'~': 3, '*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '=': 0}

    @staticmethod
    def tokenize(program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

    def input(self, expression):
        tokens = tokenize(expression)
        unarified_tokens = self.unarify(tokens)
        rpn_expression = self.gen_rpn(unarified_tokens)
        return self.eval_rpn(rpn_expression)

    def parse_variable(self, var):
        if var in self.vars:
            return self.vars[var]
        raise ValueError(f"ERROR: Invalid identifier. No variable with name '{var}' was found.")

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

    @staticmethod
    def unarify(expression: list) -> list:
        unary = True
        unarified_expression = []
        for token in expression:
            if unary and token in ('+', '-'):
                unary = False
                if token == '+':
                    continue
                elif token == '-':
                    token = '~'
            elif token in ('+', '-', '*', '/', '%', '(', '='):
                unary = True
            else:
                unary = False
            unarified_expression.append(token)

        return unarified_expression

    def eval_rpn(self, expression: list):
        if not expression:
            return ''
        stack = MyStack()
        for token in expression:
            if token in self.binary_operators:
                y, x = stack.pop(), stack.pop()
                x = self.parse_variable(x) if type(x) is str else x
                y = self.parse_variable(y) if type(y) is str else y
                if x is None or y is None:
                    raise ValueError('Bad syntax! One of the operands is of type None')
                x = self.calculate(x, y, token)
                stack.push(x)
            elif token == '~':
                x = stack.pop()
                x = self.parse_variable(x) if type(x) is str else x
                if x is None:
                    raise ValueError('Bad syntax! One of the operands is of type None')
                stack.push(-x)
            elif token == '=':
                y, x = stack.pop(), stack.pop()
                if type(x) is not str:
                    raise ValueError(f'{x} is not variable!')
                y = self.parse_variable(y) if type(y) is str else y
                self.vars[x] = y
                stack.push(y)
            elif type(token) in [int, float, str]:
                stack.push(token)
            else:
                raise ValueError(f'Unexpected token: {token}')
        result = stack.pop()
        result = self.parse_variable(result) if type(result) is str else result
        if result is None or not stack.is_empty():
            raise ValueError(f"rpn-result is '{result}' (must not be None) and stack is {stack.stack} (must be empty)!")
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
                        raise ValueError("No left parenthesis '(' was found!")
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

    def rpn_to_ast(self, rpn_expression):
        stack = MyStack()
        for token in rpn_expression:
            if token in self.binary_operators:
                b, a = stack.pop(), stack.pop()
                stack.push({'op': token, 'a': a, 'b': b})
            elif token == '~':
                b = stack.pop()
                stack.push({'op': '-', 'a': {'op': 'imm', 'n': 0}, 'b': b})
            elif token in self.args:
                stack.push({'op': 'arg', 'n': self.args[token]})
            else:
                stack.push({'op': 'imm', 'n': token})

        return stack.pop()

    def process_arg_list(self, t_program):
        n_args, pos = 0, 0
        for token in t_program:
            pos += 1
            if token == '[':
                continue
            elif token == ']':
                break
            else:
                self.args[token] = n_args
                n_args += 1

        return t_program[pos:]

    def pass1(self, prog):
        t_prog = self.tokenize(prog)
        t_expr = self.process_arg_list(t_prog)
        u_expr = self.unarify(t_expr)
        rpn = self.gen_rpn(u_expr)
        print(rpn)
        ast = self.rpn_to_ast(rpn)
        return ast

    def pass2(self, ast):
        def traverse(tree):
            if 'a' in tree:
                a_subtree, b_subtree = tree['a'], tree['b']
                traverse(a_subtree)
                traverse(b_subtree)
                if a_subtree['op'] == 'imm' and b_subtree['op'] == 'imm':
                    tree['n'] = self.calculate(a_subtree['n'], b_subtree['n'], tree['op'])
                    del tree['a']
                    del tree['b']
                    tree['op'] = 'imm'
        traverse(ast)
        return ast

    def translate(self, node):
        op = node['op']
        if op in self.binary_operators:
            return self.translate_bin_op(node)
        elif op == 'imm':
            return f'IM {node["n"]}'
        elif op == 'arg':
            return f'AR {node["n"]}'

    def translate_bin_op(self, node):
        a = self.translate(node['a'])
        b = self.translate(node['b'])
        asm = [a, 'PU', b, 'SW', 'PO'] if type(a) is list else [b, 'SW', a]
        op = node['op']
        if op == '*':
            return asm + ['MU']
        elif op == '/':
            return asm + ['DI']
        elif op == '+':
            return asm + ['AD']
        elif op == '-':
            return asm + ['SU']

    def pass3(self, ast):
        asm = []

        def flat(lst):
            for item in lst:
                if type(item) is list:
                    flat(item)
                else:
                    asm.append(item)
        flat(self.translate(ast))
        return asm


def test0():
    interpreter = Interpreter()
    prog = '[x y z w] (y + z) * (w + x)'
    print(prog)
    print(ast1 := interpreter.pass1(prog))
    print(ast2 := interpreter.pass2(ast1))
    print(asm := interpreter.pass3(ast2))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
