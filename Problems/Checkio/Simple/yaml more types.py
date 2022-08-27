# https://py.checkio.org/ru/mission/yaml-more-types/

def parse(value):
    if value in ('null', ''):
        return None
    if value == 'false':
        return False
    if value == 'true':
        return True
    value = value.replace('\\"', '"')
    value = value.replace("\\'", "'")
    if (value[0] == '"' and value[-1] == '"') or (value[0] == "'" and value[-1] == "'"):
        value = value[1:-1]

    return value


def yaml(yaml_text):
    return {key: int(value) if value.isdigit() else parse(value)
            for key, value in [map(str.strip, line.split(':')) for line in yaml_text.split('\n') if line]}


def test0():
    print(yaml('name: Alex\nage: 12'))
    print(yaml('name: Alex Fox\n'
               'age: 12\n'
               '\n'
               'class: 12b'))
    print(yaml('name: "Alex Fox"\n'
               'age: 12\n'
               '\n'
               'class: 12b'))
    print(yaml('name: "Alex \\"Fox\\""\n'
               'age: 12\n'
               '\n'
               'class: 12b'))
    print(yaml('name: "Bob Dylan"\n'
               'children: 6\n'
               'alive: false'))
    print(yaml('name: "Bob Dylan"\n'
               'children: 6\n'
               'coding:'))
    print(yaml('name: "Bob Dylan"\n'
               'children: 6\n'
               'coding: null'))
    print(yaml('name: "Bob Dylan"\n'
               'children: 6\n'
               'coding: "null" '))


def test1():
    print("Example:")
    print(yaml('name: Alex\nage: 12'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml('name: Alex\nage: 12') == {'age': 12, 'name': 'Alex'}
    assert yaml('name: Alex Fox\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex Fox"\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex Fox'}
    assert yaml('name: "Alex \\"Fox\\""\n'
                'age: 12\n'
                '\n'
                'class: 12b') == {'age': 12,
                                  'class': '12b',
                                  'name': 'Alex "Fox"'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'alive: false') == {'alive': False,
                                    'children': 6,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding:') == {'children': 6,
                               'coding': None,
                               'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: null') == {'children': 6,
                                    'coding': None,
                                    'name': 'Bob Dylan'}
    assert yaml('name: "Bob Dylan"\n'
                'children: 6\n'
                'coding: "null" ') == {'children': 6,
                                       'coding': 'null',
                                       'name': 'Bob Dylan'}
    print("Coding complete? Click 'Check' to earn cool rewards!")


def test2():
    pass


if __name__ == '__main__':
    test0()
    test1()
    test2()
