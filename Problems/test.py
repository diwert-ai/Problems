﻿def flatten(dictionary):
    res_dict = dict()

    def parse_dict(dic, in_key=''):
        if not dic:
            res_dict[in_key] = ''
            return
        for key in dic:
            val = dic[key]
            new_key = in_key + '/' + key if in_key != '' else in_key + key
            if type(val) is dict:
                parse_dict(val, new_key)
            else:
                res_dict.update({new_key: val})

    parse_dict(dictionary)
    return res_dict


def test0():
    test_input = {"key": {"deeper": {"more": {"enough": "value"}}}}
    print(' Input: {}'.format(test_input))
    print('Output: {}'.format(flatten(test_input)))

    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten(
        {"key": {"deeper": {"more": {"enough": "value"}}}}
    ) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({"name": {
        "first": "One",
        "last": "Drone"},
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"}}}
    ) == {"name/first": "One",
          "name/last": "Drone",
          "job": "scout",
          "recent": "",
          "additional/place/zone": "1",
          "additional/place/cell": "2"}
    print('You all set. Click "Check" now!')


def test1():
    print(flatten({"empty": {}}))


if __name__ == '__main__':
    test0()
