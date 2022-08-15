def yaml(yaml_text):
    return {key: int(value) if value.isdigit() else value
            for key, value in [map(str.strip, line.split(':')) for line in yaml_text.split('\n') if line]}


def test0():
    print("Example:")
    print(yaml("""name: Alex
age: 12"""))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12, 'class': '12b', 'name': 'Alex Fox'}
    print("Coding complete? Click 'Check' to earn cool rewards!")


def test1():
    r = '   asm asf    '
    print(r.strip() + r.strip())


if __name__ == '__main__':
    test0()
