from gngscrap import run_query


# генератор вычисляет декартово произведение аргументов
def product(*args):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


mapping = {'2': "abc",
           '3': "def",
           '4': "ghi",
           '5': "jkl",
           '6': "mno",
           '7': "pqrs",
           '8': "tuv",
           '9': "wxyz"}


def letter_combinations(digits):
    if not digits:
        return []
    return list(map(''.join, product(*tuple(map(lambda x: mapping[x], digits)))))


def top_k(combs):
    combs_stat = []
    for comb in combs:
        stat = run_query(comb)[0][1]
        combs_stat.append((comb, sum(stat)/len(stat) if stat else 0))

    return sorted(combs_stat, key=lambda x: x[1], reverse=True)


def test0():
    tests = ('233', )
    for digits in tests:
        print(top_k(letter_combinations(digits)))


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
