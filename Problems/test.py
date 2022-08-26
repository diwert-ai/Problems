def nonogram_encode(data: list[str]) -> list:
    rows_clue = []
    for line in data:
        row_clue = []
        index = 0
        while index < len(line):
            cnt = 0
            while index < len(line) and line[index] == 'X':
                cnt += 1
                index += 1
            index += 1
            row_clue.append(cnt) if cnt else None
        rows_clue.append(row_clue)
    k = max(map(len, rows_clue))
    for i in range(len(rows_clue)):
        lr = len(rows_clue[i])
        d = k - lr
        if d:
            rows_clue[i] = [0]*d + rows_clue[i]

    first_columns_clue = []
    n = len(data[0])
    columns = [[row[i] for row in data] for i in range(n)]
    for column in columns:
        column_clue = []
        index = 0
        while index < len(column):
            cnt = 0
            while index < len(column) and column[index] == 'X':
                cnt += 1
                index += 1
            index += 1
            column_clue.append(cnt) if cnt else None
        first_columns_clue.append(column_clue)
    m = len(first_columns_clue[0])
    columns_clue = [[clue[i] for clue in first_columns_clue] for i in range(m)]

    return [columns_clue, rows_clue]


def test0():
    print("Example:")
    print(nonogram_encode([" X X ", "X X X", " X X "]))

    assert nonogram_encode([" X X ", "X X X", " X X "]) == [
        [[0, 1, 0, 1, 0], [1, 1, 1, 1, 1]],
        [[0, 1, 1], [1, 1, 1], [0, 1, 1]],
    ]
    assert nonogram_encode(["X"]) == [[[1]], [[1]]]

    print("The mission is done! Click 'Check Solution' to earn rewards!")


def test1():
    print("Example:")
    print(nonogram_encode(['XXaaaX', 'aXaXXX', 'aXaXXa', 'aaXXXa', 'aXXXXa', 'aaXaaa']))


if __name__ == '__main__':
    #test0()
    test1()
