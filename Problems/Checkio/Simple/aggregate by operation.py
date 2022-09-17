# https://py.checkio.org/ru/mission/aggregate-by-operation/

def do_calc(x, y, op):
    if op == '+':
        x += y
    elif op == '-':
        x -= y
    elif op == '*':
        x *= y
    elif op == '/':
        x = x/y if y else x
    elif op == '=':
        x = y
    return x


def aggr_operation(data: list[tuple[str, int]]) -> dict[str, int]:
    result = dict()
    for expression, value in data:
        op, key = expression[0], expression[1:]
        result.update({key: do_calc(result.get(key, 0), value, op)}) if key else None
    return {key: result[key] for key in result if result[key] != 0}


def test0():
    assert aggr_operation([('+a', 7), ('-b', 8), ('*a', 10)]) == {'a': 70, 'b': -8}
    assert aggr_operation([]) == {}
    assert aggr_operation([('+a', 5), ('+a', -5), ('-a', 5), ('-a', -5)]) == {}
    assert aggr_operation([('*a', 0), ('=a', 0), ('/a', 0), ('-a', -5)]) == {'a': 5}
    assert aggr_operation([('+a', 0), ('*b', 0), ('+', 35)]) == {}
    assert aggr_operation([('+a', -5), ('-aa', -20), ('*aa', 5)]) == {'a': -5, 'aa': 100}
    assert aggr_operation([('+a', 5), ('*a', 6), ('/a', 3), ('=a', 3)]) == {'a': 3}
    assert aggr_operation([('+a', 5), ('*a', 0)]) == {}
    print('All test0 asserts have passed!')


def test1():
    assert aggr_operation([("+a", 7), ("-b", 8), ("*a", 10)]) == {"a": 70, "b": -8}
    assert aggr_operation([]) == {}
    assert aggr_operation([("+a", 5), ("+a", -5), ("-a", 5), ("-a", -5)]) == {}
    assert aggr_operation([("*a", 0), ("=a", 0), ("/a", 0), ("-a", -5)]) == {"a": 5}
    print('All test1 asserts have passed!')


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
