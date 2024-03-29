import string
import time


def is_hh_mm(time_string):
    try:
        time.strptime(time_string, '%H:%M')
    except ValueError:
        return False
    return len(time_string) == 5


def is_dd_mm_yyyy(date_string):
    try:
        time.strptime(date_string, '%d.%m.%Y')
    except ValueError:
        return False
    return len(date_string) == 10


class HackerLanguage:
    def __init__(self):
        self.text = ''
        self.code_map = dict()
        self.decode_map = dict()
        self.code_map[' '] = '1000000'
        self.decode_map['1000000'] = ' '
        for token in string.ascii_letters:
            self.code_map[token] = f'{ord(token):b}'
            self.decode_map[f'{ord(token):b}'] = token

    def write(self, new_text):
        self.text += new_text

    def delete(self, n):
        self.text = self.text[:-n]

    def send(self):
        return ''.join([self.code_map[token] if token in self.code_map else token for token in self.text])

    def read(self, msg):
        result = []
        token_start = 0
        while token_start < len(msg):
            # may be msg[toke_start: token_start+5] is time?
            if is_hh_mm(token_code := msg[token_start: token_start+5]):
                result.append(token_code)
            # may be msg[token_start: token_start+10] is date?
            elif is_dd_mm_yyyy(token_code := msg[token_start: token_start+10]):
                result.append(token_code)
            # may be msg[token_start: token_start+7] is alpha or space?
            elif (token_code := msg[token_start:token_start+7]) in self.decode_map:
                result.append(self.decode_map[token_code])
            # else: token is just token
            else:
                result.append(token_code := msg[token_start])
            token_start += len(token_code)

        return ''.join(result)


def test0():
    hl = HackerLanguage()
    hl.write('abcdXYZ')
    print(hl.text)
    print(hl.send())
    print(hl.read("11001011101101110000111010011101100"))
    print(hl.read('111001123:59110010111.01.201111000111110010110010110000001110100'))


def test1():
    # These "asserts" using only for self-checking and not necessary for auto-testing

    message_1 = HackerLanguage()
    # noinspection SpellCheckingInspection
    message_1.write("secrit")
    message_1.delete(2)
    message_1.write("et")
    message_2 = HackerLanguage()

    assert message_1.send() == "111001111001011100011111001011001011110100"
    assert message_2.read("11001011101101110000111010011101100") == "email"

    print("Coding complete? Let's try tests!")


def test2():
    s = '01:59'
    print(is_hh_mm(s))
    d = '30.13.9999'
    print(is_dd_mm_yyyy(d))


if __name__ == '__main__':
    test0()
    test1()
    test2()
