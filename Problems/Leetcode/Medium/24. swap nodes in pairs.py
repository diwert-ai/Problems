# https://leetcode.com/problems/swap-nodes-in-pairs/
# Given a linked list, swap every two adjacent nodes and return its head.
# You must solve the problem without modifying the values in the list's nodes
# (i.e., only nodes themselves may be changed.)

from linkedlist import ListNode, getLinkedList, printLinkedList


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    # мое решение
    @staticmethod
    def swap(h, a, b, e):
        if h:
            h.next = b
        if b:
            b.next = a
        if a:
            a.next = e

    @staticmethod
    def swap_pairs(head: ListNode):
        
        if head is None or head.next is None:
            return head

        h = None
        a = head
        b = a.next
        e = b.next
        head = head.next
        while b:
            Solution.swap(h, a, b, e)
            h = a
            a = e
            b = e.next if e else None
            e = b.next if b else None
           
        return head


def test0():
    tests = [[1, 2, 3, 4], [1, 2, 3, 2, 3, 2, 3], [2, 1, 2, 1, 2, 1, 4]]
    for test in tests:
        head = getLinkedList(test)
        printLinkedList(head)
        printLinkedList(Solution.swap_pairs(head))
        print('')


if __name__ == '__main__':
    test0()

        
        
