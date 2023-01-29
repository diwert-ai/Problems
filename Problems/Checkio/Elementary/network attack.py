def capture(matrix):
    n = len(matrix)
    diagonal, not_infected = [matrix[i][i] for i in range(n)], list(range(1, n))
    for i in range(n):
        matrix[i][i] = 0
    minutes, attack = 0, matrix[0]
    while any([d > 0 for d in diagonal]):
        for i in not_infected:
            if diagonal[i] == 0:
                not_infected.remove(i)
                attack = list(map(lambda x, y: 1 if x + y > 0 else 0, attack, matrix[i]))
        diagonal = list(map(lambda x, y: x - y if x - y > 0 else 0, diagonal, attack))
        minutes += 1

    return minutes


def test0():
    capture([[0, 1, 0, 1, 0, 1],
             [1, 1, 1, 0, 0, 0],
             [0, 1, 2, 0, 0, 1],
             [1, 0, 0, 1, 1, 0],
             [0, 0, 0, 1, 3, 1],
             [1, 0, 1, 0, 1, 2]])
    pass


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 8, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 8, "Base example"
    assert capture([[0, 1, 0, 1, 0, 1],
                    [1, 1, 1, 0, 0, 0],
                    [0, 1, 2, 0, 0, 1],
                    [1, 0, 0, 1, 1, 0],
                    [0, 0, 0, 1, 3, 1],
                    [1, 0, 1, 0, 1, 2]]) == 4, "Low security"
    assert capture([[0, 1, 1],
                    [1, 9, 1],
                    [1, 1, 9]]) == 9, "Small"
    print("All asserts have passed!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()