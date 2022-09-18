# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7


# my solution
def validate_battlefield(field):
    checked = set()
    ships = {4: (0, 1), 3: (0, 2), 2: (0, 3), 1: (0, 4)}

    def find_ship(row, col):
        ship = [(row, col)]
        x, y = row + 1, col
        while x < 10 and field[x][y]:
            ship.append((x, y))
            checked.add((x, y))
            x += 1
        x, y = row, col + 1
        while y < 10 and field[x][y]:
            ship.append((x, y))
            checked.add((x, y))
            y += 1
        return ship

    def is_linear_ship(ship_to_check):
        height = len(set((point[0] for point in ship_to_check)))
        width = len(set((point[1] for point in ship_to_check)))
        return width == 1 or height == 1

    def is_correct_size_and_quantity(ship_to_check):
        size = len(ship_to_check)
        if size not in ships or ships[size][0] == ships[size][1]:
            return False
        ships[size] = (ships[size][0] + 1, ships[size][1])
        return True

    def is_correct_border(ship_to_check):
        height = len(set((point[0] for point in ship_to_check)))
        width = len(set((point[1] for point in ship_to_check)))
        head_row, head_col = ship_to_check[0]
        start_i, start_j = 1 if head_row > 0 else 0, 1 if head_col > 0 else 0
        end_i, end_j = 1 if head_row + height < 9 else 0, 1 if head_col + width < 9 else 0
        start_i, stop_i = head_row - start_i, head_row + height + end_i
        start_j, stop_j = head_col - start_j, head_col + width + end_j
        return len(ship_to_check) == sum((field[r][c] for r in range(start_i, stop_i) for c in range(start_j, stop_j)))

    def is_correct_ship(row, col):
        ship = find_ship(row, col)
        if not is_linear_ship(ship) or not is_correct_size_and_quantity(ship) or not is_correct_border(ship):
            return False
        return True

    def is_full_set_ships():
        return all((ships[ship][0] == ships[ship][1] for ship in ships))

    for i in range(10):
        for j in range(10):
            if (i, j) in checked:
                continue
            checked.add((i, j))
            if field[i][j] and not is_correct_ship(i, j):
                return False

    if not is_full_set_ships():
        return False

    return True


# best practices solution
# https://www.codewars.com/kata/reviews/5589f89794c148e42900002a/groups/561ba39888f3ea83d80000b0
def validate_battlefield_bp(field):
    n, m = len(field), len(field[0])

    def cell(i, j):
        if i < 0 or j < 0 or i >= n or j >= m:
            return 0
        return field[i][j]

    def find(i, j):
        if cell(i + 1, j - 1) or cell(i + 1, j + 1):
            return 10086
        if cell(i, j + 1) and cell(i + 1, j):
            return 10086
        field[i][j] = 2
        if cell(i, j + 1):
            return find(i, j + 1) + 1
        if cell(i + 1, j):
            return find(i + 1, j) + 1
        return 1
    num = [0] * 5
    for row in range(n):
        for col in range(m):
            if cell(row, col) == 1:
                r = find(row, col)
                if r > 4:
                    return False
                num[r] += 1
    [tmp, submarines, destroyers, cruisers, battleship] = num
    return battleship == 1 and cruisers == 2 and destroyers == 3 and submarines == 4


def test0():
    battle_field1 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    battle_field2 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(validate_battlefield(battle_field1))
    print(validate_battlefield(battle_field2))


def test1():
    battle_field1 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

    battle_field2 = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                     [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                     [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                     [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0, 0, 1, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print(validate_battlefield_bp(battle_field1))
    print(validate_battlefield_bp(battle_field2))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
