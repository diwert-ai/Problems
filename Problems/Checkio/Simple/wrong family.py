from collections import deque


def is_family(tree: list[list[str]]) -> bool:
    graph = dict()
    used = set()
    children = dict()

    def add_edge(v1, v2):
        graph[v1].add(v2) if v1 in graph else graph.update({v1: {v2}})
        graph[v2].add(v1) if v2 in graph else graph.update({v2: {v1}})
        children[v2].append(v1) if v2 in children else children.update({v2: [v1]})

    for parent, child in tree:
        add_edge(parent, child)

    used.add(tree[0][0])
    queue = deque([tree[0][0]])
    while queue:
        cur_v = queue.popleft()
        for neighbor in graph[cur_v]:
            if neighbor not in used:
                used.add(neighbor)
                queue.append(neighbor)

    if len(used) != len(graph):
        return False

    for child in children:
        if len(children[child]) > 1:
            return False
        if children[child][0] in children and children[children[child][0]][0] == child:
            return False

    return True


def test0():
    print(is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]))
    print(is_family([['Logan', 'William'], ['Mike', 'Alexander'], ['William', 'Alexander']]))
    print(is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]))
    print(is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]]))
    print(is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]))


def test1():
    print("Example:")
    print(
        is_family(
            [
                ["Jack", "Mike"],
                ["Logan", "Mike"],
                ["Logan", "Jack"],
            ]
        )
    )

    assert is_family([["Logan", "Mike"]]) is True
    assert is_family([["Logan", "Mike"], ["Logan", "Jack"]]) is True
    assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Alexander"]]) is True
    assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Logan"]]) is False
    assert is_family([["Logan", "Mike"], ["Logan", "Jack"], ["Mike", "Jack"]]) is False
    assert (
            is_family([["Logan", "William"], ["Logan", "Jack"], ["Mike", "Alexander"]]) is False
    )
    assert is_family([["Jack", "Mike"], ["Logan", "Mike"], ["Logan", "Jack"]]) is False

    print("The mission is done! Click 'Check Solution' to earn rewards!")


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
