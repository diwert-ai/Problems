﻿def filter_word(word):
    result = ''
    for token in word:
        if token not in result:
            result += token
    return result


def checkio(data):
    res = ''
    graph = dict()

    for word in data:
        f_word = filter_word(word)
        for i in range(len(f_word)-1):
            token = f_word[i]
            next_token = f_word[i+1]
            if token in graph:
                graph[token].add(next_token)
            else:
                graph[token] = set(next_token)
        if f_word[-1] not in graph:
            graph[f_word[-1]] = set()

    while graph:
        start_set = set(graph)
        for vertex in graph:
            start_set -= graph[vertex]
        start_vertex = sorted(start_set)[0]
        res += start_vertex
        del graph[start_vertex]

    return res


def test0():
    assert checkio(["acb", "bd", "zwa"]) == "zwacbd", "Just concatenate it"
    assert checkio(["klm", "kadl", "lsm"]) == "kadlsm", "Paste in"
    assert (
        checkio(["a", "b", "c"]) == "abc"
    ), "Cant determine the order - use english alphabet"
    assert checkio(["aazzss"]) == "azs", "Each symbol only once"
    assert checkio(["dfg", "frt", "tyg"]) == "dfrtyg", "Concatenate and paste in"
    print('all asserts have passed!')


def test1():
    print(checkio(["abd", "zxy", "rtu"]))
    print(checkio(["axton", "bxton"]))
    print(checkio(["ghi", "abc", "def"]))


if __name__ == '__main__':
    test0()
    test1()
