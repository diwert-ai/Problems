# https://contest.yandex.ru/contest/49847/problems/D/
# В генеалогическом древе у каждого человека, кроме родоначальника, есть ровно один родитель.
#
# Каждом элементу дерева сопоставляется целое неотрицательное число, называемое высотой. У родоначальника высота равна
# 0, у любого другого элемента высота на 1 больше, чем у его родителя.
#
# Вам дано генеалогическое древо, определите высоту всех его элементов.

def calc_levels(human_pairs):
    tree, ancestor, result = dict(), set(), list()
    for child, parent in human_pairs:
        tree[child] = parent

        if parent not in tree:
            ancestor.add(parent)

        if child in ancestor:
            ancestor.discard(child)

    tree[ancestor.pop()] = None

    for human in sorted(tree):
        level, child = 0, tree[human]

        while child:
            level += 1
            child = tree[child]

        result.append((human, level))

    return result


def test0():
    test_data = ((('Alexei', 'Peter_I'),
                  ('Anna', 'Peter_I'),
                  ('Elizabeth', 'Peter_I'),
                  ('Peter_II', 'Alexei'),
                  ('Peter_III', 'Anna'),
                  ('Paul_I', 'Peter_III'),
                  ('Alexander_I', 'Paul_I'),
                  ('Nicholaus_I', 'Paul_I')), )
    for pairs in test_data:
        print(*calc_levels(pairs))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
