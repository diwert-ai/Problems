# https://py.checkio.org/en/mission/nonogram-encode/
# https://en.wikipedia.org/wiki/Nonogram

# you already have a binary image, formed by strings of equal length,
# where background empty cell is whitespace and picture cell filled with 'X'.
# Your goal is to create a nonogram from the image: write a number clue for
# solving this image like it was hidden. Your function should return a list of
# two lists. The first one consists of lists with numbers for columns clue,
# the second one - the same for rows clue. All lists in columns clue, as well
# as in rows, should be of same 'depth' (complemented with 0)

def zero_padding(lists):
    max_list_len = max(map(len, lists))
    for list_index in range(len(lists)):
        diff = max_list_len - len(lists[list_index])
        if diff:
            lists[list_index] = [0]*diff + lists[list_index]


def get_clues(lists):
    result = []
    for lst in lists:
        lst_clue, index = [], 0
        while index < len(lst):
            cnt = 0
            while index < len(lst) and lst[index] == 'X':
                cnt += 1
                index += 1
            index += 1
            lst_clue.append(cnt) if cnt else None
        result.append(lst_clue)
    zero_padding(result)
    return result


def nonogram_encode(data: list[str]) -> list:
    rows_clues = get_clues(data)
    n = len(data[0])
    columns = [[row[i] for row in data] for i in range(n)]
    preliminary_columns_clues = get_clues(columns)
    m = len(preliminary_columns_clues[0])
    columns_clues = [[clue[i] for clue in preliminary_columns_clues] for i in range(m)]
    return [columns_clues, rows_clues]


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
    test0()
    test1()
