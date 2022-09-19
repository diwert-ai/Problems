digits = '12345678'
letters = 'abcdefgh'


def chess_knight(start, moves):
    cell_set = set()

    def get_moves(start_cell, rest_of_moves):
        if rest_of_moves:
            letter_start, digit_start = start_cell
            i, j = letters.index(letter_start), digits.index(digit_start)
            ij = ((i + 2, j + 1), (i + 2, j - 1), (i - 2, j + 1), (i - 2, j - 1),
                  (i + 1, j + 2), (i + 1, j - 2), (i - 1, j + 2), (i - 1, j - 2))
            for k, l in ij:
                if -1 < k < 8 and -1 < l < 8:
                    cell = letters[k] + digits[l]
                    cell_set.add(cell)
                    get_moves(cell, rest_of_moves-1)
    get_moves(start, moves)
    return sorted(cell_set)


def test0():
    print(chess_knight('a1', 1))
    print(chess_knight('h8', 2))


def test1():
    print("Example:")
    print(chess_knight('a1', 1))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert chess_knight('a1', 1) == ['b3', 'c2']
    assert chess_knight('h8', 2) == ['d6', 'd8', 'e5', 'e7', 'f4', 'f7', 'f8', 'g5', 'g6', 'h4', 'h6', 'h8']
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
