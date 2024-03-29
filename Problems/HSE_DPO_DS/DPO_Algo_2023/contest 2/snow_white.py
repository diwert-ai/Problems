# https://contest.yandex.ru/contest/49329/problems/A/
# У Белоснежки очень много гномов, она даже не знает сколько. И все гномы разного роста, но Белоснежка знает, что рост
# каждого гнома не менее 100 и не более 150 сантиметров.
#
# Сегодня Белоснежка хочет узнать рост самого высокого и второго по росту гнома. Напишите программу, которая поможет ей
# узнать эту информацию.
#
# Формат ввода:
# Вводятся целые числа, каждое в новой строке. Последним идёт число 0.
# Гарантируется, что до 0 будет введено хотя бы два числа, соответствующих ограничениям на рост гнома.
#
# Формат вывода:
# Выведите два числа – рост самого высокого и второго по росту гномов, каждое с новой строки.
#
# Примечания:
# Использовать стандартные методы для поиска - нельзя!!! Здесь также не стоит использовать сортировку.
# Белоснежка надеется, что предложенное Вами решение не потребует хранения в памяти компьютера всех введённых чисел, но
# в связи с тем, что проблема очень актуальна, подойдёт любое решение.

def top2_dwarfs(heights):
    max_height, second_height, current_height = -1, -1, -1

    for current_height in heights:
        if current_height > max_height:
            second_height = max_height
            max_height = current_height
        elif current_height > second_height:
            second_height = current_height

    return max_height, second_height


def top2_dwarfs_streamed():
    max_height, second_height, current_height = -1, -1, -1

    while current_height:
        if current_height > max_height:
            second_height = max_height
            max_height = current_height
        elif current_height > second_height:
            second_height = current_height

        current_height = int(input())

    return max_height, second_height


def test0():
    tests = ((1, 5, 3, 10, 11, 20, 21),
             (1, 2, 3, 3, 3, 3),
             (1, 2, 3, 3, -10, 100, 99),
             (5, 5, 5, 5),
             (1, 1))

    for test_array in tests:
        print(*top2_dwarfs(test_array))


def test1():
    print(*top2_dwarfs_streamed())


if __name__ == '__main__':
    for test in (test0, test1):
        test()
