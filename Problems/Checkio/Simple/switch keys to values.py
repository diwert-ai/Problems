# https://py.checkio.org/en/mission/switch-keys-to-values/

def switch_dict(data: dict) -> dict:
    res = dict()
    for key in data:
        res[value].add(str(key)) if (value := str(data[key])) in res else res.update({value: set([str(key)])})
    return res


def test0():
    print(switch_dict({"rouses": "red", "car": "red", "sky": "blue"}))
    print(switch_dict({1: "number", 2: "number", 3: "number"}))


def test1():
    print("Example:")
    print(switch_dict({"rouses": "red", "car": "red", "sky": "blue"}))

    assert switch_dict({"rouses": "red", "car": "red", "sky": "blue"}) == {
        "red": {"car", "rouses"},
        "blue": {"sky"},
    }
    assert switch_dict({1: 1, 2: 2, 3: 3, 4: 4}) == {
        "1": {"1"},
        "2": {"2"},
        "3": {"3"},
        "4": {"4"},
    }

    print("The mission is done! Click 'Check Solution' to earn rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
