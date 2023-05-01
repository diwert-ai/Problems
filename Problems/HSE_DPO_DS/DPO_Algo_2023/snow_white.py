# https://contest.yandex.ru/contest/49329/problems/A/
# У Белоснежки очень много гномов, она даже не знает сколько. И все гномы разного роста, но Белоснежка знает, что рост
# каждого гнома не менее 100 и не более 150 сантиметров.
#
# Сегодня Белоснежка хочет узнать рост самого высокого и второго по росту гнома. Напишите программу, которая поможет ей
# узнать эту информацию.

def top2_dwarfs(heights):
    max_height, second_height, current_height = -1, -1, -1

    for current_height in heights:
        if current_height > max_height:
            second_height = max_height
            max_height = current_height
        elif current_height > second_height:
            second_height = current_height

    return max_height, second_height


def test():
    tests = ((1, 5, 3, 10, 11, 20, 21),
             (1, 2, 3, 3, 3, 3),
             (1, 2, 3, 3, -10, 100, 99),
             (5, 5, 5, 5),
             (1, 1))

    for test_array in tests:
        print(*top2_dwarfs(test_array))


if __name__ == '__main__':
    test()
