# Найти наибольшую общую подстроку
# ABABC и BABCA -> BABC

def lcs(s1, s2):
    n1, n2 = len(s1), len(s2)
    dp = [[0] * (n2 + 1) for _ in range(n1+1)]

    for i in range(1, n1 + 1):
        for j in range(1, n2 + 1):
            cur_len = dp[i - 1][j - 1]
            if s1[i-cur_len-1:i] == s2[j-cur_len-1:j]:
                dp[i][j] = cur_len + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs_len = dp[-1][-1]
    for i in range(n1-lcs_len+1):
        for j in range(n2-lcs_len+1):
            if s1[i:i+lcs_len] == s2[j:j+lcs_len]:
                return s1[i:i+lcs_len], lcs_len


def test0():
    test_data = (('ABABC', 'BABCA'), ('abfgfgrfgfguba', 'abadfgfgfgufgwfs'))
    for s1, s2 in test_data:
        print(lcs(s1, s2))


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
