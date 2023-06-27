# union-find задача

# наивный подход
def find(a, color):
    """
    Возвращает номер множества (цвет),
    в котором лежит элемент a.
    """
    return color[a]


def union_naive(a, b, color):
    """
    Присоединяется множество, в котором лежит элемент b,
    к множеству, в котором лежит элемент a.
    """
    color_a = color[a]
    color_b = color[b]
    for i in range(len(color)):
        if color[i] == color_b:
            color[i] = color_a

# Всего можно сделать n-1 операций union (с аргументами из разных множеств)
# до полного объединения и в каждой операции цикл O(n) - т.е. полная асимптотика O(n^2)


def test0():
    print('-------naive-test------')
    n = 8
    color = [i for i in range(n)]
    print(*color)
    print(find(6, color))
    union_naive(1, 5, color)
    union_naive(2, 6, color)
    union_naive(6, 5, color)
    print(*color)
    print(find(6, color))


# Улучшение асимптотики до О(log n) (в среднем на запрос find) можно добиться путем 1) осуществление присоединения
# (всегда) меньшего множества к большему 2) созданием дополнительной структуры данных, которая по номеру множества
# возвращает список его элементов.


def union_boost(a, b, color, color_list):
    color_a, color_b = color[a], color[b]
    if len(color_list[color_a]) < len(color_list[color_b]):
        color_a, color_b = color_b, color_a

    for element in color_list[color_b]:
        color[element] = color_a

    color_list[color_a] += color_list[color_b]
    color_list[color_b] = []


def test1():
    print('----union-find-boost-test---')
    n = 8
    color = [i for i in range(n)]
    color_list = [[i] for i in range(n)]
    print(*color)
    print(*color_list)
    print(find(6, color))
    union_boost(1, 5, color, color_list)
    union_boost(2, 6, color, color_list)
    union_boost(6, 5, color, color_list)
    union_boost(7, 5, color, color_list)
    print(*color)
    print(find(6, color))
    print(*color_list)


# Дальнейшее улучшение - это метод DSU. Система непересекающихся множеств. Асимптотика O(log n) на один запрос find
# или union в среднем. Вводится список предков parents. Каждое множество организовано
# как дерево, которое хранится в parents. Номер множества - это элемент, который хранится в корне. Для любого корня
# верно parents[root]:=root. Проводится сжатие путей внутри функции find. (Также можно добавить ранговую эвристику и
# приклеивать меньшее дерево к большему тогда асимптотика достигнет  O(\alpha(N)) (обратная функция
# Аккермана - почти О(1)) - тут подробнее https://e-maxx.ru/algo/dsu)

def find_dsu(a, parents):
    """
    Возвращает корень дерева, в котором лежит элемент a (все деревья хранятся в списке предков parents. Одно дерево =
    одно множество)
    """
    root = a
    while parents[root] != root:
        root = parents[root]

    # делаем сжатие путей
    while parents[a] != a:
        next_element = parents[a]
        parents[a] = root
        a = next_element

    return root


def union_dsu(a, b, parents):
    """
    Объединяет дерево a с деревом b, присоединяя корень одного к корню другого
    """
    parents[find_dsu(a, parents)] = find_dsu(b, parents)


def test2():
    print('-------dsu-test-----')
    n = 8
    parents = [i for i in range(n)]
    print(*parents)
    print(find_dsu(6, parents))
    union_dsu(1, 5, parents)
    union_dsu(2, 6, parents)
    union_dsu(6, 5, parents)
    union_dsu(7, 5, parents)
    print(*parents)
    print(find_dsu(2, parents))
    print(*parents)


if __name__ == '__main__':
    tests = (test0, test1, test2)
    for test in tests:
        test()
