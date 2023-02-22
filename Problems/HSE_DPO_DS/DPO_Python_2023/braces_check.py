def braces_check(string):
    # будем использовать list как стек (добавлять и удалять элементы стека можно только с конца),
    # в котором будут храниться только открывающие скобки
    stack = list()
    for brace in string:  # обрабатываем каждую скобку последовательности по очереди
        if brace in '({[':  # если встретилась открывающая скобка, то кладем ее в стек
            stack.append(brace)
        else:
            # если же встретилась закрывающая скобка, то делаем следующее:
            if not stack:  # если стек пустой, то последовательность неправильная
                return False  # и возвращаем False

            left_brace = stack.pop()  # вытаскиваем из стека открывающую скобку
            if ((brace == ')' and left_brace != '(')  # если открывающая и закрывающая скобки разных типов, то
                    or (brace == '}' and left_brace != '{')  # последовательность неправильная и возвращаем False
                    or (brace == ']' and left_brace != '[')):
                return False

    # если после обработки всех скобок стек пустой, значит последовательность правильная
    return not stack


def test0():
    seqs = ('[({})]', '[({)]', '{}', '{{}}[', '{}([])', '(())[{]}', '[({)]')
    for seq in seqs:
        print(f'seq: {seq} {braces_check(seq)}')


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
