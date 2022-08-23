# https://py.checkio.org/ru/mission/flatten-list/
# Существует список, который содержит целые числа или другие
# вложенные списки, которые могут содержать ещё несколько списков
# и целых чисел, которые затем... ну, вы поняли. Вы должны поместить
# все целые значения в один плоский список. Порядок должен быть такой же,
# как и в первоначальном списке, с представлением строки слева направо.

def flat_list(array):
    ret = []

    def parse_lst(lst):
        for item in lst:
            ret.append(item) if type(item) is not list else parse_lst(item)
    parse_lst(array)
    return ret


if __name__ == '__main__':
    assert flat_list([1, 2, 3]) == [1, 2, 3], "First"
    assert flat_list([1, [2, 2, 2], 4]) == [1, 2, 2, 2, 4], "Second"
    assert flat_list([[[2]], [4, [5, 6, [6], 6, 6, 6], 7]]) == [2, 4, 5, 6, 6, 6, 6, 6, 7], "Third"
    assert flat_list([-1, [1, [-2], 1], -1]) == [-1, 1, -2, 1, -1], "Four"
    print('Done! Check it')
