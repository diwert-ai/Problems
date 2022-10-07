# https://py.checkio.org/ru/mission/find-quotes/
# Ваша задача сейчас - найти все цитаты в тексте. Ну, и как это уже принято,
# сделать все как можно быстрее.
# Вам дана строка, которая состоит из символов и парного количества кавычек.
# Необходимо вернуть массив (Iterable) из текстов внутри кавычек.
# Необходимы цитаты только с использованием двойных кавычек (").
# Одинарные кавычки (') не подходят.
def find_quotes(text):
    quotes, i, n = [], 0, len(text)
    while i < n:
        if text[i] == '"':
            j = i + 1
            while j < n and text[j] != '"':
                j += 1
            if text[j] == '"':
                quotes.append(text[i+1:j])
            i = j + 1
        else:
            i += 1
    return quotes


def test0():
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []


def test1():
    print("Example:")
    print(find_quotes('"Greetings"'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
                       'of the printing and typesetting '
                       'industry. Lorem Ipsum has been the '
                       '"industry\'s standard dummy text '
                       'ever since the 1500s", when an '
                       'unknown printer took a galley of '
                       'type and scrambled it to make a type '
                       'specimen book. It has survived not '
                       'only five centuries, but also the '
                       'leap into electronic typesetting, '
                       'remaining essentially unchanged. "It '
                       'was popularised in the 1960s" with '
                       'the release of Letraset sheets '
                       'containing Lorem Ipsum passages, and '
                       'more recently with desktop '
                       'publishing software like Aldus '
                       'PageMaker including versions of '
                       'Lorem Ipsum.') == ['Lorem Ipsum',
                                           "industry's standard dummy text ever "
                                           'since the 1500s',
                                           'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
