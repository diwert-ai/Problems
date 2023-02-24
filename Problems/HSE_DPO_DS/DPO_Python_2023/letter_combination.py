from gngscrap import run_query  # модуль для получения частоты N-граммы в виде JSON ответа
                                # от сервиса Google Ngram Viewer


# генератор вычисляет декартово произведение аргументов
def product(*args):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


# соответствие цифр и букв на кнопочном телефоне
mapping = {'2': "abc",
           '3': "def",
           '4': "ghi",
           '5': "jkl",
           '6': "mno",
           '7': "pqrs",
           '8': "tuv",
           '9': "wxyz"}


# возвращает возможные комбинации по набору цифр
def letter_combinations(digits):
    if not digits:
        return []
    return list(map(''.join, product(*tuple(map(lambda x: mapping[x], digits)))))


# возвращает топ k=5 комбинаций букв (n-грамм) отсортированных по убыванию частоты
def top_k(combs, k=5):
    combs_stat = []
    for comb in combs:
        try:
            stat = run_query(comb)[0][1]
        except:
            stat = None
        combs_stat.append((comb, sum(stat) / len(stat) if stat else 0))

    return sorted(combs_stat, key=lambda x: x[1], reverse=True)[:k]


def test0():
    tests = ('4663', )
    for digits in tests:
        print(top_k(letter_combinations(digits), k=5))

    # out: [('good', 0.0004746672944747843), ('home', 0.00027761877281591297),
    # ('gone', 9.665996567491675e-05), ('hood', 5.133915249189158e-06), ('hoof', 1.184510261964533e-06)]


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
