from requests import get, JSONDecodeError
from urllib import parse


# генератор вычисляет декартово произведение аргументов
def product(*args):
    # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
    pools = [tuple(pool) for pool in args]
    result = [[]]
    for pool in pools:
        result = [x + [y] for x in result for y in pool]
    for prod in result:
        yield tuple(prod)


# выполняет запрос к сервису https://books.google.com и возвращает json
# если он вернулся от сервиса
# навеяно этим: https://www.geeksforgeeks.org/scrape-google-ngram-viewer-using-python/
def run_query(query, start_year=2000,
              end_year=2019, corpus=26,
              smoothing=0):
    # converting a regular string to the standard URL format
    # eg: "geeks for,geeks" will convert to "geeks%20for%2Cgeeks"
    query = parse.quote(query)
    url = 'https://books.google.com/ngrams/json?content=' + query + \
          '&year_start=' + str(start_year) + '&year_end=' + \
          str(end_year) + '&corpus=' + str(corpus) + '&smoothing=' + \
          str(smoothing) + ''

    return get(url).json()


# возвращает топ k=5 комбинаций букв (n-грамм) отсортированных по убыванию частоты
def top_k_ngrams(numeric_code, k=5):
    mapping = {'2': "abc", '3': "def", '4': "ghi", '5': "jkl", '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"}
    ngrams = list(map(''.join, product(*tuple(map(lambda x: mapping[x], numeric_code)))))
    ngrams_stat, ngrams_num, chunk_size = [], len(ngrams), 512
    print(f'combinations total: {ngrams_num},  chunk size: {chunk_size}')
    for chunk_start in range(0, ngrams_num, chunk_size):
        print(f'processing combinations from {chunk_start} to {chunk_start + chunk_size}...')
        request = ','.join(ngrams[chunk_start:chunk_start + chunk_size])
        try:
            data = run_query(request)
        except JSONDecodeError:
            print('JSONDecodeError is appeared!')
            data = None

        for num, rec in enumerate(data, start=1):
            ngram, stat = rec['ngram'], rec['timeseries']
            freq = sum(stat) / len(stat) if stat else 0
            print(f'#{num} stats for "{rec["ngram"]}" is {freq}')
            ngrams_stat.append((ngram, sum(stat) / len(stat) if stat else 0))
    print(f'ngrams with stats total: {len(ngrams_stat)}')
    return sorted(ngrams_stat, key=lambda x: x[1], reverse=True)[:k]


def test0():
    tests = ('4663', )
    for digits in tests:
        if digits:
            print(top_k_ngrams(digits))

    # out: [('good', 0.0004746672944747843), ('home', 0.00027761877281591297),
    # ('gone', 9.665996567491675e-05), ('hood', 5.133915249189158e-06), ('hoof', 1.184510261964533e-06)]


if __name__ == '__main__':
    test_funcs = (test0,)
    for test in test_funcs:
        test()
