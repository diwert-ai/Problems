# рекурсивный вывод слияния двух отсортированных списков
def merge_print0(a, b):
    if len(a) == 0:
        for x in b:
            print(x, end=' ')
        print('')
        return

    if len(b) == 0:
        for x in a:
            print(x, end=' ')
        print('')
        return

    if a[0] > b[0]:
        print(b[0], end=' ')
        merge_print0(a, b[1:])
    else:
        print(a[0], end=' ')
        merge_print0(a[1:], b)

    return


# нерекурсивный вывод слияния двух отсортированных списков
def merge_print1(a, b):
    if len(a) == 0:
        for x in b:
            print(x, end=' ')
        print('')
        return

    if len(b) == 0:
        for x in a:
            print(x, end=' ')
        print('')
        return

    i_a = i_b = 0

    while i_a < len(a) and i_b < len(b):
        if a[i_a] < b[i_b]:
            print(a[i_a], end=' ')
            i_a += 1
        else:
            print(b[i_b], end=' ')
            i_b += 1

    if i_a == len(a):
        for x in b[i_b:]:
            print(x, end=' ')
    else:
        for x in a[i_a:]:
            print(x, end=' ')
    print('')


if __name__ == '__main__':
    a_lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    b_lst = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    merge_print0(a_lst, b_lst)
    merge_print1(a_lst, b_lst)
