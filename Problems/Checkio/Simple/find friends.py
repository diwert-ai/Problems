# https://py.checkio.org/en/mission/find-friends/
# Дан массив прямых связей между дронами - кто с кем дружит.
# Каждая такая связь представлена, как строка с двумя именами
# разделенными дефисом. Для примера: "dr101-mr99" означает что dr101 и mr99
# дружат между собой. Кроме этого даны два имени. Попробуйте определить,
# связаны ли они через других дронов, вне зависимости от глубины этих связей.

from collections import deque


def check_connection(network, first, second):
    graph, used = dict(), set()

    def add_edge(v1, v2):
        graph[v1].add(v2) if v1 in graph else graph.update({v1: {v2}})
        graph[v2].add(v1) if v2 in graph else graph.update({v2: {v1}})

    def bfs(vertex):
        used.add(vertex)
        queue = deque([vertex])
        while queue:
            cur_v = queue.popleft()
            if cur_v == second:
                return True
            for neighbor in graph[cur_v]:
                if neighbor not in used:
                    used.add(neighbor)
                    queue.append(neighbor)
        return False

    for connection in network:
        add_edge(*connection.split('-'))

    return bfs(first)


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "scout2", "scout3") is True, "Scout Brotherhood"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "super", "scout2") is True, "Super Scout"
    assert check_connection(
        ("dr101-mr99", "mr99-out00", "dr101-out00", "scout1-scout2",
         "scout3-scout1", "scout1-scout4", "scout4-sscout", "sscout-super"),
        "dr101", "sscout") is False, "I don't know any scouts."

    print('All asserts have pased!')
