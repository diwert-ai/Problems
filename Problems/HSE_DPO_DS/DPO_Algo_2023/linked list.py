# реализация связанного списка

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push_begin(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    @staticmethod
    def push_after(prev, value):
        new_node = Node(value)
        new_node.next = prev.next
        prev.next = new_node

    def delete(self, value):
        if self.head.data == value:
            self.head = self.head.next
            return

        curr = self.head
        prev = None
        while curr and curr.data != value:
            prev = curr
            curr = curr.next

        if not curr:
            return
        prev.next = curr.next

    def search(self, value):
        curr = self.head
        while curr and curr.data != value:
            curr = curr.next

        if not curr:
            return None
        return curr.data

    def push_end(self, value):
        curr = self.head

        while curr.next:
            curr = curr.next

        curr.next = Node(value)

    def reverse(self):
        prev = None
        curr = self.head

        while curr:
            next_el = curr.next
            curr.next = prev
            prev = curr
            curr = next_el
        self.head = prev

    def __str__(self):
        ret = ''
        curr = self.head
        while curr:
            ret += str(curr.data) + ' '
            curr = curr.next
        return ret


def test0():
    ll = LinkedList()
    # 2 1 3
    ll.push_begin(1)
    ll.push_begin(2)
    ll.push_end(3)
    ll.push_end(4)
    ll.push_end(5)
    ll.push_after(ll.head, 6)
    ll.push_after(ll.head.next, 7)
    print(ll)
    ll.reverse()
    print(ll)
    ll.delete(2)
    print(ll)
    ll.delete(4)
    print(ll)
    ll.reverse()
    print(ll)


if __name__ == '__main__':
    tests = (test0,)
    for test in tests:
        test()
