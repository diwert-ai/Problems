# https://www.codewars.com/kata/5265b0885fda8eac5900093b
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


class Compiler:
    def __init__(self):
        self.args = {}
        self.binary_operators = ('+', '-', '*', '/')
        self.operators = ('+', '-', '*', '/', '~')
        self.precedence = {'~': 3, '*': 2, '/': 2, '+': 1, '-': 1}

    def compile(self, program):
        return self.pass3(self.pass2(self.pass1(program)))

    @staticmethod
    def tokenize(program):
        """Turn a program string into an array of tokens.  Each token
           is either '[', ']', '(', ')', '+', '-', '*', '/', a variable
           name or a number (as a string)"""
        token_iter = (m.group(0) for m in re.finditer(r'[-+*/()[\]]|[A-Za-z]+|\d+', program))
        return [int(tok) if tok.isdigit() else tok for tok in token_iter]

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
            elif token in ('+', '-', '*', '/', '('):
                unary = True
            else:
                unary = False
            unarified_expression.append(token)

        return unarified_expression

    def gen_rpn(self, expression: list):
        """Shunting yard algorithm by Edsger Dijkstra
        https://en.wikipedia.org/wiki/Shunting_yard_algorithm
        """
        out = []
        stack = MyStack()
        for token in expression:
            if token in self.operators:
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


def simulate(asm, argv):
    r0, r1, n = None, None, None
    stack = []
    for ins in asm:
        if ins[:2] == 'IM' or ins[:2] == 'AR':
            ins, n = ins[:2], int(ins[2:])
        if ins == 'IM':
            r0 = n
        elif ins == 'AR':
            r0 = argv[n]
        elif ins == 'SW':
            r0, r1 = r1, r0
        elif ins == 'PU':
            stack.append(r0)
        elif ins == 'PO':
            r0 = stack.pop()
        elif ins == 'AD':
            r0 += r1
        elif ins == 'SU':
            r0 -= r1
        elif ins == 'MU':
            r0 *= r1
        elif ins == 'DI':
            r0 /= r1
    return r0


def test0():
    compiler = Compiler()
    prog = '[x y z] (x * (y/(z-(x/(10 + z)) + z * (10 - x))))*(x-y-z)'
    print(prog)
    print(asm := compiler.compile(prog))
    argv = x, y, z = 123, -212, -3212
    print(simulate(asm, argv), (x * (y / (z - (x / (10 + z)) + z * (10 - x))))*(x-y-z))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
