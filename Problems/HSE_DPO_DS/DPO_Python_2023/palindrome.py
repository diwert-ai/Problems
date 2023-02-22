def palindrome(n):
    # если число отрицательное - сразу возвращаем `False`
    if n < 0:
        return False

    # для неотрицательных целых найдем сначала "обращение"
    tmp, invert_n = n, 0
    while tmp >= 1:
        invert_n = 10 * invert_n + tmp % 10
        tmp //= 10

    # если число и обращение совпали, то значит число палиндром
    return n == invert_n


# s = 'fabvbbaf'
# Решение для строк без использования дополнительной памяти
# (s == s[::-1] требует доп. память!)

def palindrome_str(s):
    half_len_s = len(s)//2

    for i in range(half_len_s):
        if s[i] != s[-i-1]:
            return False

    return True


def test0():
    tests = (121132, 2938012, 29380128003100,78987, 987898789,
             -1239281731, -128739871298738917268, 11111111111111111211111111111111111)
    for number in tests:
        print(f'{number}: {palindrome(number)}')


def test1():
    tests = ('sakdj', 'aksjdha', 'abccba', 'qwertrewq')
    for string in tests:
        print(f'{string}: {palindrome_str(string)}')


if __name__ == '__main__':
    test_funcs = (test0, test1)
    for test in test_funcs:
        test()
