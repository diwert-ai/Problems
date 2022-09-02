roman = {'I': 1,
         'V': 5,
         'X': 10,
         'L': 50,
         'C': 100,
         'D': 500,
         'M': 1000}
first = {
    '0': "",
    '1': "I",
    '2': "II",
    '3': "III",
    '4': "IV",
    '5': "V",
    '6': "VI",
    '7': "VII",
    '8': "VIII",
    '9': "IX"}
second = {
    '0': "",
    '1': "X",
    '2': "XX",
    '3': "XXX",
    '4': "XL",
    '5': "L",
    '6': "LX",
    '7': "LXX",
    '8': "LXXX",
    '9': "XC",
}
third = {
    '0': "",
    '1': "C",
    '2': "CC",
    '3': "CCC",
    '4': "CD",
    '5': "D",
    '6': "DC",
    '7': "DCC",
    '8': "DCCC",
    '9': "CM",
}
forth = {
    '0': "",
    '1': "M",
    '2': "MM",
    '3': "MMM",
}


class RomanNumerals:

    @staticmethod
    def to_roman(val):
        lv = list(f'{val:04d}')
        return f'{forth[lv[0]]}{third[lv[1]]}{second[lv[2]]}{first[lv[3]]}'

    @staticmethod
    def from_roman(roman_num):
        result = 0
        list_s = list(roman_num)
        n = len(list_s)
        for i in range(n - 1):
            d_i = roman[list_s[i]]
            if d_i >= roman[list_s[i + 1]]:
                result += d_i
            else:
                result -= d_i
        result += roman[list_s[n - 1]]
        return result


def test0():
    print(RomanNumerals.from_roman('X'), RomanNumerals.to_roman(3999))


def test1():
    pass


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
