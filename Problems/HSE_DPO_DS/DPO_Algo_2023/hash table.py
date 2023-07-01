# реализация hash таблицы

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):  # O(1)
        return hash(key) % self.capacity

    def insert(self, value):  # O(1), O(size)
        index = self._hash(value)
        if not self.table[index]:
            self.table[index] = Node(index, value)
            self.size += 1
        else:
            current = self.table[index]
            while current.next:  # None
                current = current.next
            current.next = Node(index, value)
            self.size += 1

    def search(self, value):  # O(1), O(size)
        index = self._hash(value)
        current = self.table[index]
        while current:
            if current.value == value:
                return current.value
            current = current.next
        raise KeyError(value)

    def remove(self, value):  # O(1), O(size)
        index = self._hash(value)
        current = self.table[index]
        prev = None
        while current:
            if current.value == value:
                if prev:
                    prev.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            prev = current
            current = current.next
        raise KeyError(value)

    def __contains__(self, key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False

    def __len__(self):
        return self.size

    def __str__(self):
        str_p = ''
        for i in range(self.capacity):
            str_p += str(i) + ' '
            current = self.table[i]
            while current:
                str_p += current.value + ' '
                current = current.next
            str_p += '\n'
        return str_p


def test0():
    hash_table = HashTable(10)
    hash_table.insert("apple")
    hash_table.insert("notebook")
    hash_table.insert("row")
    print(hash_table.search("apple"))
    print(hash_table.search("notebook"))
    print(hash_table.search("row"))
    hash_table.insert("pow")
    hash_table.insert("hat")
    hash_table.insert("pool")
    hash_table.insert("join")
    hash_table.insert("len")
    print(hash_table)
    hash_table.remove("hat")
    hash_table.remove("len")
    print(hash_table)
    hash_table.remove("notebook")
    print(hash_table)
    print(len(hash_table))
    print("the" in hash_table)
    print("pow" in hash_table)
    if "111" in hash_table:
        hash_table.remove("111")


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
