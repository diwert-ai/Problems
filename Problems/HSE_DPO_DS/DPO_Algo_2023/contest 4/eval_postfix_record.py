# https://contest.yandex.ru/contest/49847/problems/B/
# В постфиксной записи (или обратной польской записи) операция записывается после двух операндов. Например, сумма двух
# чисел A и B записывается как A B +. Запись B C + D * обозначает привычное нам (B + C) * D, а запись A B C + D * +
# означает A + (B + C) * D. Достоинство постфиксной записи в том, что она не требует скобок и дополнительных соглашений
# о приоритете операторов для своего чтения.

def eval_postfix_record(tokens):
    stack = list()
    ops = {'+': lambda x, y: x + y, '-': lambda x, y: y - x, '*': lambda x, y: x * y}
    for token in tokens:
        stack.append(ops[token](stack.pop(), stack.pop()) if token in ops else int(token))
    return stack.pop()


def test0():
    postfix_records = ('8 9 + 1 7 - *', '1 2 * 3 4 + +')
    for rec in postfix_records:
        print(eval_postfix_record(rec.split()))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
