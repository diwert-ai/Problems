# https://py.checkio.org/ru/mission/unix-match-part-1/
# Ваша задача - определить, соответствует ли заданное имя файла
# заданному поисковому паттерну.
# *    соответствует всему (любому количеству любых символов)
# ?	соответствует любому одному символу


# мое решение
def unix_match(filename: str, pattern: str) -> bool:
    if not pattern:
        return not filename

    first_match = bool(filename) and pattern[0] in [filename[0], '?']

    if pattern[0] == '*':
        return (unix_match(filename, pattern[1:]) or
                (bool(filename) and unix_match(filename[1:], pattern)))
    else:
        return first_match and unix_match(filename[1:], pattern[1:])


if __name__ == '__main__':
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') is True
    assert unix_match('other.exe', '*') is True
    assert unix_match('my.exe', '*.txt') is False
    assert unix_match('log1.txt', 'log?.txt') is True
    assert unix_match('log12.txt', 'log?.txt') is False
    assert unix_match('log12.txt', 'log??.txt') is True
    print("Coding complete? Click 'Check' to earn cool rewards!")
