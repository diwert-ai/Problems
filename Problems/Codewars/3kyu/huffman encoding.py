import heapq


class BNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def __add__(self, other):
        return BNode((self.value[0]+other.value[0], self.value[1] + other.value[1]))

    def __lt__(self, other):
        return self.value[::-1] < other.value[::-1]

    def __repr__(self):
        return str(self.value)


# noinspection SpellCheckingInspection
def h_tree(freqs):
    nodes = list(map(lambda x: BNode(x), freqs))
    heapq.heapify(nodes)
    root = nodes[0]
    while len(nodes) > 1:
        right, left = heapq.heappop(nodes), heapq.heappop(nodes)
        root = right + left
        root.left, root.right = left, right
        heapq.heappush(nodes, root)
    return root


# takes: str; returns: [ (str, int) ] (Strings in return value are single characters)
def frequencies(s: str):
    return [(char, s.count(char)) for char in set(s)]


# takes: [ (str, int) ], str; returns: String (with "0" and "1")
# noinspection SpellCheckingInspection
def encode(freqs, s):
    if len(freqs) < 2:
        return None
    root, codes = h_tree(freqs), dict()

    def pre_order(node: BNode, code=''):
        if node:
            codes[node.value[0]] = code
            pre_order(node.left, code+'0')
            pre_order(node.right, code+'1')
    pre_order(root)
    return ''.join((codes[char] for char in s))


# takes [ [str, int] ], str (with "0" and "1"); returns: str
# noinspection SpellCheckingInspection
def decode(freqs, bits):
    if len(freqs) < 2:
        return None
    root = h_tree(freqs)
    cur_node, decode_s = root, ''
    for bit in bits:
        cur_node = cur_node.left if bit == '0' else cur_node.right
        if len(c := cur_node.value[0]) == 1:
            decode_s += c
            cur_node = root
    return decode_s


def test0():
    # noinspection SpellCheckingInspection
    s = 'jldaksjdlkasjdlkasdiuyeruiyertmbndmsbfmnbmnbxcjgjhsdfas'
    print(s)
    f = frequencies(s)
    print(f)
    encode_s = encode(f, s)
    print(encode_s)
    decode_s = decode(f, encode_s)
    print(decode_s)


# noinspection SpellCheckingInspection
def test1():
    a = BNode(('a', 10))
    b = BNode(('b', 20))
    print(a+b)
    freqs = [('a', 1)]
    nodes = list(map(lambda x: BNode(x), freqs))
    print(nodes[0])


if __name__ == '__main__':
    test_funcs = [test0, test1]
    for test in test_funcs:
        test()
