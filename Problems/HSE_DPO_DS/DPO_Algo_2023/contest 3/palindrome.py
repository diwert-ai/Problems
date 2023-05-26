# https://contest.yandex.ru/contest/49613/problems/F/
# На вход программы поступает набор больших латинских букв (необязательно различных). Разрешается переставлять буквы,
# а также удалять некоторые буквы. Требуется из данных букв по указанным правилам составить палиндром наибольшей длины,
# а если таких палиндромов несколько, то выбрать первый из них в алфавитном порядке.

def palindrome(string):
    counts = [0] * 26
    middle_index = -1

    for char in string:
        counts[ord(char) - 65] += 1

    for i in range(26):
        if counts[i] % 2 and (middle_index == -1 or i < middle_index):
            middle_index = i

    result = ''.join(chr(i + 65) * (counts[i] // 2) for i in range(26))
    middle = chr(middle_index + 65) if middle_index > -1 else ''

    return result + middle + result[::-1]


def test0():
    strings = ('AAB', 'QAZQAZ', 'QQZFRQSBGU', 'EEXEIABMBN', 'TBKZOOKMAK')
    for string in strings:
        print(palindrome(string))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
