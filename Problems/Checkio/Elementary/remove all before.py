# https://py.checkio.org/en/mission/remove-all-before/
from typing import Iterable


def remove_all_before_my(items: list, border: int) -> Iterable:
    # your code here
    if items:
        return []

    i = 0
    while i < len(items):
        if items[i] == border:
            break
        i += 1

    return items if i == len(items) else items[i:]


def remove_all_before(items: list, border: int) -> Iterable:
    # your code here
    return items[items.index(border):] if border in items else items


if __name__ == '__main__':
    print("Example:")
    print(list(remove_all_before([1, 2, 3, 4, 5], 3)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(remove_all_before([1, 2, 3, 4, 5], 3)) == [3, 4, 5]
    assert list(remove_all_before([1, 1, 2, 2, 3, 3], 2)) == [2, 2, 3, 3]
    assert list(remove_all_before([1, 1, 2, 4, 2, 3, 4], 2)) == [2, 4, 2, 3, 4]
    assert list(remove_all_before([1, 1, 5, 6, 7], 2)) == [1, 1, 5, 6, 7]
    assert list(remove_all_before([], 0)) == []
    assert list(remove_all_before([7, 7, 7, 7, 7, 7, 7, 7, 7], 7)) == [7, 7, 7, 7, 7, 7, 7, 7, 7]
    print("Coding complete? Click 'Check' to earn cool rewards!")
