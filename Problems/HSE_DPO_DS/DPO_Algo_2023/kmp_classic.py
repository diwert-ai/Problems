# Алгоритм Кнута-Морриса-Пратта

def prefix_function(s):
    n = len(s)
    prefix = [0] * n
    cur_p = 0

    for i in range(1, n):
        while cur_p > 0 and s[cur_p] != s[i]:
            cur_p = prefix[cur_p - 1]
        if s[i] == s[cur_p]:
            cur_p += 1
        prefix[i] = cur_p

    return prefix


def kmp(t, p):
    n = len(t)
    m = len(p)
    result = []
    p_array = prefix_function(p)
    count = 0
    for i in range(n):
        while count > 0 and p[count] != t[i]:
            count = p_array[count-1]
        if p[count] == t[i]:
            count += 1
        if count == m:
            result.append((i - m + 1, i))
            count = p_array[count-1]

    return result


def test0():
    test_data = (('abababaxaba', 'baxa'), )
    for t, p in test_data:
        print(kmp(t, p))


if __name__ == '__main__':
    tests = (test0, )
    for test in tests:
        test()
