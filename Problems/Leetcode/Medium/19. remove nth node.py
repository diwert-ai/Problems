# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# Definition for singly-linked list.
from linkedlist import ListNode


class Solution:
    @staticmethod
    def remove_nth_from_end(head: ListNode, n: int):
        if n <= 0:
            return head

        if head is None:
            return None

        node_n = head
        h = {}
        sz = 1
        
        while node_n.next:
            h[sz] = node_n
            sz += 1
            node_n = node_n.next
        
        h[sz] = node_n

        if n > sz:
            return None
        
        if n == 1 and sz == 1:
            return None
        else:
            if n == 1:
                h[sz-1].next = None
            elif n == sz:
                head = h[2]
            else:
                h[sz-n].next = h[sz-n+2]

        return head


def get_linked_list(lst):
    n = len(lst)
    if n == 0:
        return None
    h = ListNode(val=lst[0])
    c = h
    for i in range(1, n):
        c.next = ListNode(val=lst[i])
        c = c.next
    return h


def get_list(lst):
    r = []
    c = lst
    while c:
        r.append(c.val)
        c = c.next
    return r


def print_linked_list(lst):
    c = lst
    while c:
        print(c.val, end=' ')
        c = c.next


def test0():
    print_linked_list(get_linked_list([1, 3, 2, 4, 2, 4]))


def test1():
    t = [1, 4, 3, 2, 3, 3]
    r = get_list(get_linked_list(t))
    print(r)
    print(t == r)


def test2():
    lst = [-1]
    n = -1
    linked_l = get_linked_list(lst)
    r = Solution.remove_nth_from_end(linked_l, n)
    print(lst)
    print(get_list(r))
  

if __name__ == '__main__':
    test0()
    test1()
    test2()
    
