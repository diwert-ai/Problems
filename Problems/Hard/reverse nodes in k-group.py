#https://leetcode.com/problems/reverse-nodes-in-k-group/

#Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

#k is a positive integer and is less than or equal to the length of the linked list. 
#If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

#You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from lib.linkedlist import ListNode, getLinkedList, printLinkedList

class Solution:
    def inverseLinkedList(self,lst:ListNode, new_head:ListNode = None):

        end  = lst        
        while end.next != None:
            prev = end
            end = end.next

        if new_head == None: 
            new_head = end

        end.next = prev
        prev.next = None

        if lst.next != None:
            return self.inverseLinkedList(lst,new_head)
        else:
            return new_head
        
    def inverse_segment(self, prev:ListNode,lst:ListNode,post:ListNode):

        end = lst

        if post != None:
            while not (end.next is post):
                end = end.next
        else:
            while end.next != None:
                end = end.next

        end.next = None

        new_lst = self.inverseLinkedList(lst)

        if prev != None:
            prev.next = new_lst

        new_end = lst
        new_end.next = post

        if prev == None:
            return new_lst
        else:
            return None
        
    def inverse_segment_i(self, lst:ListNode,left_bound_index:int,right_bound_index:int):
        if right_bound_index - left_bound_index < 3:
            return

        prev,post = lst,lst

        if left_bound_index<0:
            prev = None
            seg = lst
        else:
            for i in range(left_bound_index):
                prev = prev.next
            seg = prev.next

        for i in range(right_bound_index):
            if post == None:
                break
            post = post.next
            
        return self.inverse_segment(prev,seg,post)

    #мое решение (медленное и запутанное)        
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        cur = head
        l = 0
        while(cur.next):
            cur = cur.next
            l += 1

        start = -1
        stop = start + k + 1

        while stop < l+2:           
            n_head = self.inverse_segment_i(head,start,stop)
            head = n_head if n_head != None else head
            start = stop-1
            stop = start + k + 1

        return head
    #решение https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
    #Succinct iterative Python, O(n) time O(1) space
    def reverseKGroupL(self, head, k):
        dummy = jump = ListNode(0)
        dummy.next = l = r = head
    
        while True:
            count = 0
            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next

def test0():
    lst = getLinkedList([i for i in range(20)])
    printLinkedList(lst)
    printLinkedList(Solution().reverseKGroup(lst,4))
    lst = getLinkedList([i for i in range(20)])
    printLinkedList(lst)
    printLinkedList(Solution().reverseKGroupL(lst,4))




if __name__ == '__main__':
    test0()
        
