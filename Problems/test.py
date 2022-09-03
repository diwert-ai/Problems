# https://www.codewars.com/kata/526d84b98f428f14a60008da
# my solution
class Hash:
    hash = {1: 1}
    m = 1


def hamming(n):
    if n in Hash.hash:
        return Hash.hash[n]

    for i in range(Hash.m+1, n+1):
        g_i = Hash.hash[i-1]
        h_i = 2 * g_i
        for j in range(1, i):
            h_j = Hash.hash[j]
            if h_i > 2*h_j > g_i:
                h_i = 2 * h_j
            elif h_i > 3*h_j > g_i:
                h_i = 3 * h_j
            elif h_i > 5*h_j > g_i:
                h_i = 5 * h_j
        Hash.hash[i] = h_i
        Hash.m += 1
    return Hash.hash[n]


# best practices
# https://www.codewars.com/kata/526d84b98f428f14a60008da/solutions/python
def hamming_bp(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]


def test0():
    print(hamming(1004))


def test1():
    print(hamming_bp(1004))


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
