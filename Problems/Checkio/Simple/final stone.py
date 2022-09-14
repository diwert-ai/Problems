# https://py.checkio.org/en/mission/the-final-stone/
# Your goal is to find the weight of the final stone. If no stones left, the result is 0.
#
# The algorith is very simple:
#
# get the two biggest stones in the batch
# hit and get the resulting stone
# put the resulting stone back in the batch.
# For the Speedy category, you can think about your solution for a million stones

def left_bound(array: list, key):
    left = -1
    right = len(array)

    while right - left > 1:
        middle = (left + right) // 2
        if array[middle] < key:
            left = middle
        else:
            right = middle

    return left


def final_stone(stones: list[int]) -> int:
    if stones:
        stones.sort()
        for _ in range(len(stones)-1):
            new_stone = stones[-1] - stones[-2]
            left = left_bound(stones[:-2], new_stone) + 1
            stones = stones[:left] + [new_stone] + stones[left:-2]
        return stones[0]
    return 0


def test0():
    final_stone([3, 5, 1, 1, 9])
    final_stone([1, 2, 3, 4])
    # s = [4] * (1000*1000)
    # final_stone(s)


def test1():
    print('Example:')
    print(final_stone([1, 2, 3]))

    assert final_stone([3, 5, 1, 1, 9]) == 1
    assert final_stone([1, 2, 3]) == 0
    assert final_stone([1, 2, 3, 4]) == 0
    assert final_stone([1, 2, 3, 4, 5]) == 1
    assert final_stone([1, 1, 1, 1]) == 0
    assert final_stone([1, 1, 1]) == 1
    assert final_stone([1, 10, 1]) == 8
    assert final_stone([1, 10, 1, 8]) == 0
    assert final_stone([]) == 0
    assert final_stone([1]) == 1
    assert final_stone([10, 20, 30, 50, 100, 10, 20, 10]) == 10

    print("The mission is done! Click 'Check Solution' to earn rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
