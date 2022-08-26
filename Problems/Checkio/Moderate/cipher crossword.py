# https://py.checkio.org/ru/mission/cipher-crossword/
# Дан пустой кроссворд, как 2-х мерный массив с числами, где 0 - это
# пустая клетка, а остальные числа соответствуют зашифрованным буквам.
# Также дан список слов для кроссворда. Вы должны заполнить кроссворд
# и вернуть решенный кроссворд, как 2-х мерный массив с буквами.
# Пустые клетки замените пробелами (0 => " ").
# Слова размещаются в строках и столбцах, но не в диагоналях. Кроссворд
# состоит из 6 слов, каждое из 5 букв.
# Входные данные: Кроссворд, как список (list) списков с числами. Слова, как список строк.
# Выходные данные: Решение кроссворда, как список списков с буквами.


from itertools import permutations


def match(word, decode, code_dict):
    for position, key in enumerate(decode):
        if key in code_dict:
            if code_dict[key] != word[position]:
                return False
        else:
            value = word[position]
            if value in code_dict.values():
                return False
            else:
                code_dict[key] = value
    return True


def checkio(crossword, words):
    def find(perm):
        perm = tuple(perm)
        for num in range(n):
            if not match(words[perm[num]], ext_crossword[num], code_dict):
                return False
        return True
    n = len(words)
    code_dict = dict()
    ext_crossword = [crossword[2*i] for i in range(n//2)]
    for i in range(n//2):
        ext_crossword.append([row[2*i] for row in crossword])
    for permutation in permutations((0, 1, 2, 3, 4, 5)):
        code_dict = dict()
        if find(permutation):
            break
    code_dict[0] = ' '
    return [[code_dict[row[col]] for col in range(n-1)] for row in crossword]


def test0():
    assert checkio(
        [
            [21, 6, 25, 25, 17],
            [14, 0, 6, 0, 2],
            [1, 11, 16, 1, 17],
            [11, 0, 16, 0, 5],
            [26, 3, 14, 20, 6],
        ],
        ["hello", "habit", "lemma", "ozone", "bimbo", "trace"],
    ) == [
        ["h", "e", "l", "l", "o"],
        ["a", " ", "e", " ", "z"],
        ["b", "i", "m", "b", "o"],
        ["i", " ", "m", " ", "n"],
        ["t", "r", "a", "c", "e"],
    ]
    assert checkio([
                    [19, 23, 22, 1, 23],
                    [8, 0, 9, 0, 6],
                    [10, 1, 6, 2, 22],
                    [13, 0, 8, 0, 18],
                    [22, 21, 18, 13, 22]
                ],
                ['users', 'crime', 'eagle', 'uncle', 'eking', 'siege']
    ) == [
                ['u', 's', 'e', 'r', 's'],
                ['n', ' ', 'k', ' ', 'i'],
                ['c', 'r', 'i', 'm', 'e'],
                ['l', ' ', 'n', ' ', 'g'],
                ['e', 'a', 'g', 'l', 'e'],
            ]

    # noinspection SpellCheckingInspection
    assert checkio([
                    [14, 9, 24, 10, 14],
                    [24, 0, 13, 0, 13],
                    [13, 26, 13, 20, 18],
                    [6, 0, 25, 0, 9],
                    [14, 6, 9, 3, 14]
                ],
                ['sodas', 'loofa', 'slots', 'stars', 'ovoid', 'sales']
    ) == [
                ['s', 'a', 'l', 'e', 's'],
                ['l', ' ', 'o', ' ', 'o'],
                ['o', 'v', 'o', 'i', 'd'],
                ['t', ' ', 'f', ' ', 'a'],
                ['s', 't', 'a', 'r', 's'],
         ]


if __name__ == '__main__':
    test0()
