# https://py.checkio.org/en/mission/fast-train/
# You are planning the train schedule, and you want to know the minimum time of traveling between the stations.
# Each section of the rail between stations is given in the list. Each section is a tuple of distance and
# speed limit (both are integers). You can change the speed ( +1. -1 and ± 0 ) at the start and every minute
# after that. The train runs by the same amount as the speed value in a minute.
# Note: This means that a train with a speed 2 will travel a distance 2 before another minute passes and its
# speed can be changed again.
# Starting speed is 0.
# Speed limit is set for each section of the rail. You don't exceed it.
# You must reach the target station at speed 1 (because it’s necessary to stop at the station).
# You should return the minimum time (minutes) as an integer.

def fast_train(sections):
    result, velocity_max, total_distance = 0, [], 0
    for section_length, section_v_max in sections:
        velocity_max += [section_v_max] * section_length
        total_distance += section_length
    distance_reminder, velocity, cur_pos = total_distance, 1, 1

    def check(u, x_start):
        """check if speed u is possible on section [x_start:x_start+u]"""
        return u * (u + 1) / 2 <= distance_reminder and all(u <= w for w in velocity_max[x_start:x_start + u])

    while distance_reminder > 0:
        distance_reminder -= velocity
        velocity = velocity + 1 if check(velocity + 1, cur_pos) else \
            (velocity if check(velocity, cur_pos) else velocity - 1)
        cur_pos, result = cur_pos + velocity, result + 1
    return result


def test0():
    sections = [(8, 2), (8, 10), (8, 4)]
    print(fast_train(sections))


def test1():
    print("Example:")
    print(fast_train([(4, 3)]))

    assert fast_train([(4, 3)]) == 3
    assert fast_train([(9, 10)]) == 5
    assert fast_train([(5, 5), (4, 2)]) == 6
    print("Coding complete? Click 'Check' to earn cool rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
