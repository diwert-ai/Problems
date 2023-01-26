# https://py.checkio.org/en/mission/fibonacci-poem/

def fibo_poem(text: str) -> str:
    if text == '':
        return ''
    result, fibo_series, words = '', fibo_series_generator(), text.split()
    current_linebreak_index, previous_linebreak_index, num_words = next(fibo_series), 0, len(words)
    for word_index in range(num_words):
        result += words[word_index]
        if word_index + 1 == current_linebreak_index:
            result += '\n'
            previous_linebreak_index = current_linebreak_index
            current_linebreak_index += next(fibo_series)
        else:
            result += ' '
    if num_words == previous_linebreak_index:
        current_linebreak_index = previous_linebreak_index
    return result[:-1] + (current_linebreak_index-num_words)*' _'


def fibo_series_generator():
    last_two_fibo_nums = [1, 1]
    yield last_two_fibo_nums[0]
    yield last_two_fibo_nums[1]
    while True:
        next_fibo_num = sum(last_two_fibo_nums)
        last_two_fibo_nums[0], last_two_fibo_nums[1] = last_two_fibo_nums[1], next_fibo_num
        yield next_fibo_num


def test0():
    print(fibo_poem("Django framework"))
    print(fibo_poem("Zen of Python"))
    pass


def test1():
    print("Example:")
    print(fibo_poem("Zen of Python"))

    # These "asserts" are used for self-checking
    assert fibo_poem("") == ""
    assert fibo_poem("Django framework") == "Django\nframework"
    assert fibo_poem("Zen of Python") == "Zen\nof\nPython _"
    assert (
            fibo_poem("There are three kinds of lies: Lies, damned lies, and the benchmarks.")
            == "There\nare\nthree kinds\nof lies: Lies,\ndamned lies, and the benchmarks."
    )

    print("The mission is done! Click 'Check Solution' to earn rewards!")
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
