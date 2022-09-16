# https://www.codewars.com/kata/5671d975d81d6c1c87000022

from itertools import permutations

skyscrapers = dict()


def get_clue(tpl):
    clue = 1
    if tpl[1] > tpl[0]:
        clue = 2
    if tpl[2] > max(tpl[0], tpl[1]):
        clue += 1
    if tpl[3] > max(tpl[0], tpl[1], tpl[2]):
        clue += 1
    return clue


def calc_all_clues(p1, p2, p3, p4):
    columns = tuple((p1[i], p2[i], p3[i], p4[i]) for i in range(4))
    rows = (p1, p2, p3, p4)
    clues1 = (get_clue(columns[i]) for i in range(4))
    clues2 = (get_clue(rows[i][::-1]) for i in range(4))
    clues3 = (get_clue(columns[i][::-1]) for i in range(3, -1, -1))
    clues4 = (get_clue(rows[i]) for i in range(3, -1, -1))
    skyscrapers[(*clues1, *clues2, *clues3, *clues4)] = (p1, p2, p3, p4)


def fill_skyscrapers_dict():
    for perm1 in permutations((1, 2, 3, 4)):
        for perm2 in permutations((1, 2, 3, 4)):
            if any((perm1[i] == perm2[i] for i in range(4))):
                continue
            for perm3 in permutations((1, 2, 3, 4)):
                if any((perm3[i] in (perm1[i], perm2[i]) for i in range(4))):
                    continue
                perm4 = tuple((10 - perm1[i] - perm2[i] - perm3[i] for i in range(4)))
                calc_all_clues(perm1, perm2, perm3, perm4)


fill_skyscrapers_dict()


def solve_puzzle(clues):
    def filter_by_clues(clues_to_find):
        return all(clues_to_find[i] == clue for i, clue in enumerate(clues) if clue != 0)
    full_clues = tuple(filter(filter_by_clues, skyscrapers.keys()))[0]
    return skyscrapers[full_clues]


def test0():
    fill_skyscrapers_dict()


def test1():
    print(skyscrapers[(2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3)])
    tests_clues = [(0, 0, 1, 2, 0, 2, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0),
                   (2, 2, 1, 3, 2, 2, 3, 1, 1, 2, 2, 3, 3, 2, 1, 3)]

    for test_clues in tests_clues:
        print(solve_puzzle(test_clues))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
