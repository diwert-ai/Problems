#https://leetcode.com/problems/merge-two-sorted-lists/
#You are given the heads of two sorted linked lists list1 and list2.
#Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
#Return the head of the merged linked list.

from linkedlist import *

#Definition for singly-linked list.
#class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self):
        self.head = None
        self.end  = None

    #мое решение
    def mergeTwoListsMy(self, list1: ListNode, list2: ListNode) -> ListNode:
        
        def merge(l1,l2):
            if l1 == None:
                self.end.next = l2 
                return self.head
            
            if l2 == None:
                self.end.next = l1
                return self.head
            
            if l1.val > l2.val:
                self.end.next = l2
                self.end = l2
                merge(l1,l2.next)
            else:
                self.end.next = l1
                self.end = l1
                merge(l1.next,l2)
            
            return self.head
        
        if list1 == None: return list2
        
        if list2 == None: return list1
        
        if list1.val > list2.val:
            self.head = self.end = list2
            return merge(list1,list2.next)
        
        self.head = self.end = list1
        return merge(list1.next,list2)
    
    #решение most votes
    #https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained
    #Time: O(n)
    #Space: O(1)
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        cur = dummy = ListNode()
        while list1 and list2:               
            if list1.val < list2.val:
                cur.next = list1
                list1, cur = list1.next, list1
            else:
                cur.next = list2
                list2, cur = list2.next, list2
                
        if list1 or list2:
            cur.next = list1 if list1 else list2
            
        return dummy.next

def test0():
    l1 = [1,2,3,4,5,6]
    l2 = [1,2,3,4,5,6,7,8,9]   
    list1 = getLinkedList(l1)
    list2 = getLinkedList(l2)
    printLinkedList(list1)
    printLinkedList(list2)
    #list3 = Solution().mergeTwoLists(list1,list2)
    #printLinkedList(list1)
    #printLinkedList(list2)
    list4 = Solution().mergeTwoListsMy(list1,list2)
    printLinkedList(list1)
    printLinkedList(list2)
    #printLinkedList(list3)
    printLinkedList(list4)

def test1():
    l  = [1,2,3,4,5]
    for i in l[1:]:
        print(i)

def test2():
    l = [1,2,3,4,5,6]
    list1 = getLinkedList(l)
    printLinkedList(list1)
    printLinkedList(list1)
  


 

if __name__ == '__main__':
    test0()

        
        

