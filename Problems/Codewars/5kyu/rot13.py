# https://www.codewars.com/kata/530e15517bc88ac656000716/python
# ROT13 is a simple letter substitution cipher that replaces a
# letter with the letter 13 letters after it in the alphabet.
# ROT13 is an example of the Caesar cipher.
# Create a function that takes a string and returns the string ciphered with Rot13.
# If there are numbers or special characters included in the string,
# they should be returned as they are. Only letters from the latin/english alphabet
# should be shifted, like in the original Rot13 "implementation".
# Please note that using encode is considered cheating.

# noinspection SpellCheckingInspection
letters = 'abcdefghijklmnopqrstuvwxyz'


def rot13(message):
    def code(x, alphabet=letters):
        return alphabet[(alphabet.index(x)+13) % 26] if x.isalpha() else x
    return ''.join(code(x) if x.islower() else code(x, letters.upper()) for x in message)


# noinspection SpellCheckingInspection
def tests():
    assert rot13('test') == 'grfg'
    assert rot13('Test') == 'Grfg'
    assert rot13('aA bB zZ 1234 *!?%') == 'nN oO mM 1234 *!?%'


if __name__ == '__main__':
    tests()
