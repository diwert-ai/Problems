#https://leetcode.com/problems/swap-nodes-in-pairs/
#Given a linked list, swap every two adjacent nodes and return its head. 
#You must solve the problem without modifying the values in the list's nodes 
#(i.e., only nodes themselves may be changed.)

from lib.linkedlist import *


# Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    #мое решение
    def swap(self,h,a,b,e):
        if h: h.next = b
        if b: b.next = a
        if a: a.next = e
            
    def swapPairs(self, head: ListNode) -> ListNode:
        
        if head == None or head.next == None:
            return head
        

        h = None
        a = head
        b = a.next
        e = b.next
        head = head.next
        while b:
            self.swap(h,a,b,e)
            h = a
            a = e
            b = e.next if e else None
            e = b.next if b else None
           
        return head

def test0():
    tests = [[1,2,3,4], [1,2,3,2,3,2,3],[2,1,2,1,2,1,4]]
    for test in tests:
        head = getLinkedList(test)
        printLinkedList(head)
        printLinkedList(Solution().swapPairs(head))
        print('')


if __name__ == '__main__':
    test0()

        
        
