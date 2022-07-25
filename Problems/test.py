count = 0

def unix_match(filename: str, pattern: str) -> bool:
    global count 
    count += 1
    if not pattern:
        return not filename

    first_match = bool(filename) and pattern[0] in [filename[0], '?']

    if pattern[0] == '*':
        return unix_match(filename, pattern[1:]) or (bool(filename) and unix_match(filename[1:], pattern))
    else:
        return first_match and unix_match(filename[1:], pattern[1:])






if __name__ == '__main__':
    '''
    print("Example:")
    print(unix_match('somefile.txt', '*'))
    # These "asserts" are used for self-checking and not for an auto-testing
    assert unix_match('somefile.txt', '*') == True
    assert unix_match('other.exe', '*') == True
    assert unix_match('my.exe', '??.txt') == False
    assert unix_match('log1.txt', 'log?.txt') == True
    assert unix_match('log12.txt', 'log?.txt') == False
    '''

    assert unix_match('teRxt*sdaskfjldsdfnerxtrhdaksjdhgfd', 'te?xt*ne?xt?*?') == True
    print(count, len('teRxt*sdaskfjldsdfnerxtrhdaksjdhgfd') * len('te?xt*ne?xt?*?'))
    count = 0
    assert unix_match_dp('teRxt*sdaskfjldsdfnerxtrhdaksjdhgfd', 'te?xt*ne?xt?*?') == True
    print(count, len('teRxt*sdaskfjldsdfnerxtrhdaksjdhgfd') * len('te?xt*ne?xt?*?'))
    assert unix_match('l?l', '??') == False
    print("Coding complete? Click 'Check' to earn cool rewards!")