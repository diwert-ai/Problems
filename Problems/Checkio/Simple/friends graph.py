# https://py.checkio.org/ru/mission/friends/
class Friends:
    def __init__(self, connections):
        self.graph = dict()
        for connection in connections:
            self.add(connection)

    def add(self, connection):
        v1, v2 = (v for v in connection)
        if not self.in_graph(v1, v2):
            self.graph.update({v1: {v2}}) if v1 not in self.graph else self.graph[v1].add(v2)
            self.graph.update({v2: {v1}}) if v2 not in self.graph else self.graph[v2].add(v1)
            return True
        return False

    def remove(self, connection):
        v1, v2 = (v for v in connection)
        if self.in_graph(v1, v2):
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)
            return True
        return False

    def names(self):
        return {name for name in self.graph if self.graph[name]}

    def connected(self, name):
        return self.graph[name] if name in self.graph else set()

    def in_graph(self, v1, v2):
        return v1 in self.graph and v2 in self.graph[v1]


def test0():
    # These "asserts" using only for self-checking and not necessary for auto-testing
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    assert letter_friends.add({"c", "d"}) is True, "Add"
    assert letter_friends.add({"c", "d"}) is False, "Add again"
    assert letter_friends.remove({"c", "d"}) is True, "Remove"
    assert digit_friends.remove({"c", "d"}) is False, "Remove non exists"
    assert letter_friends.names() == {"a", "b", "c"}, "Names"
    assert letter_friends.connected("d") == set(), "Non connected name"
    assert letter_friends.connected("a") == {"b", "c"}, "Connected name"


def test1():
    letter_friends = Friends(({"a", "b"}, {"b", "c"}, {"c", "a"}, {"a", "c"}))
    digit_friends = Friends([{"1", "2"}, {"3", "1"}])
    letter_friends.add({"c", "d"})
    letter_friends.add({"c", "d"})
    letter_friends.remove({"c", "d"})
    digit_friends.remove({"c", "d"})
    print(letter_friends.names())
    print(letter_friends.connected("d"))
    print(letter_friends.connected("a"))
    print(letter_friends.graph)


def test2():
    f = Friends([{"And", "Or"}, {"For", "And"}])
    print(f.graph)
    print(f.add({"Or", "And"}))
    c = {'And', 'Or'}
    v1, v2 = (v for v in c)
    print(v1, v2)


if __name__ == '__main__':
    test0()
    test1()
    test2()
