# https://py.checkio.org/ru/mission/cipher-map2/
import numpy as np


def recall_password(grille, password):
    np_grille = np.array([[row[i] for i in range(4)] for row in grille]) == 'X'
    np_password = np.array([[row[i] for i in range(4)] for row in password])
    password = []
    for _ in range(4):
        password += list(np_password[np_grille])
        np_grille = np.rot90(np_grille, axes=(1, 0))
    return ''.join(password)


# noinspection SpellCheckingInspection
def test0():
    print(recall_password(['X...', '..X.', 'X..X', '....'],
                          ['itdf', 'gdce', 'aton', 'qrdi']))
    # 'icantforgetiddqd'
    print(recall_password(['....', 'X..X', '.X..', '...X'],
                          ['xhwc', 'rsqx', 'xqzz', 'fyzr']))
    # 'rxqrwsfzxqxzhczy'


# noinspection SpellCheckingInspection
def test1():
    print("Example:")
    print(recall_password(['X...', '..X.', 'X..X', '....'],
                          ['itdf', 'gdce', 'aton', 'qrdi']))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert recall_password(['X...', '..X.', 'X..X', '....'],
                           ['itdf', 'gdce', 'aton', 'qrdi']) == 'icantforgetiddqd'
    assert recall_password(['....', 'X..X', '.X..', '...X'],
                           ['xhwc', 'rsqx', 'xqzz', 'fyzr']) == 'rxqrwsfzxqxzhczy'
    print("Coding complete? Click 'Check' to earn cool rewards!")


def test2():
    pass


if __name__ == '__main__':
    test0()
    test1()
    test2()
