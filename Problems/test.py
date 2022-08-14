def checkio(text: str) -> str:
    letters = list(filter(lambda x: x.isalpha(), text.lower()))
    result = []
    max_count = 0
    for letter in set(letters):
        letter_count = letters.count(letter)
        if letter_count > max_count:
            result.clear()
            result.append(letter)
            max_count = letter_count
        elif letters.count(letter) == max_count:
            result.append(letter)
    return sorted(result)[0]


def checkio2(text: str) -> str:
    letters = list(filter(lambda x: x.isalpha(), text.lower()))
    freq_dict = {letter: letters.count(letter) for letter in set(letters)}
    leading_zeros = len(str(len(letters)))
    return sorted(freq_dict.items(), key=lambda x: f'{x[1]:0{leading_zeros}}{122-ord(x[0]):03}', reverse=True)[0][0]


def test1():
    print(checkio2('afjlsdkafmmmfa'))


if __name__ == '__main__':
    print(checkio2('Gregor then turned to look out the window at the dull weather.Nooooooooooo!!! Why!?!'))
