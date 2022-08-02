# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# k is a positive integer and is less than or equal to the length of the linked list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# You may not alter the values in the list's nodes, only nodes themselves may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional
from linkedlist import ListNode, getLinkedList, printLinkedList


class Solution:
    def inverse_linked_list(self, lst: ListNode, new_head: ListNode = None):
        end = lst
        prev = None
        while end.next is not None:
            prev = end
            end = end.next

        if new_head is None:
            new_head = end

        end.next = prev
        prev.next = None

        if lst.next is not None:
            return self.inverse_linked_list(lst, new_head)
        else:
            return new_head
        
    def inverse_segment(self, prev: ListNode, lst: ListNode, post: ListNode):

        end = lst

        if post is not None:
            while not (end.next is post):
                end = end.next
        else:
            while end.next is not None:
                end = end.next

        end.next = None

        new_lst = self.inverse_linked_list(lst)

        if prev is not None:
            prev.next = new_lst

        new_end = lst
        new_end.next = post

        if prev is None:
            return new_lst
        else:
            return None
        
    def inverse_segment_i(self, lst: ListNode, left_bound_index: int, right_bound_index: int):
        if right_bound_index - left_bound_index < 3:
            return

        prev, post = lst, lst

        if left_bound_index < 0:
            prev = None
            seg = lst
        else:
            for i in range(left_bound_index):
                prev = prev.next
            seg = prev.next

        for i in range(right_bound_index):
            if post is None:
                break
            post = post.next
            
        return self.inverse_segment(prev, seg, post)

    # мое решение (медленное и запутанное)
    def reverse_k_group(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # ищем длину списка l
        cur = head  
        length = 0
        while cur.next:
            cur = cur.next
            length += 1
        
        # последовательно инвертируем сегменты списка ограниченные индекса start и stop
        start = -1
        stop = start + k + 1

        while stop < length+2:
            n_head = self.inverse_segment_i(head, start, stop)
            head = n_head if n_head is not None else head
            start = stop-1
            stop = start + k + 1

        return head

    # решение most voted
    # https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
    # Succinct iterative Python, O(n) time O(1) space
    @staticmethod
    def reverse_k_group_mv(head, k):
        dummy = jump = ListNode(0)
        dummy.next = left = right = head
    
        while True:
            count = 0
            while right and count < k:   # use r to locate the range
                right = right.next
                count += 1
            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = right, left
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing
                jump.next, jump, left = pre, left, right  # connect two k-groups
            else:
                return dummy.next


def test0():
    lst = getLinkedList([i for i in range(20)])
    printLinkedList(lst)
    printLinkedList(Solution().reverse_k_group(lst, 4))
    lst = getLinkedList([i for i in range(20)])
    printLinkedList(lst)
    printLinkedList(Solution.reverse_k_group_mv(lst, 4))


if __name__ == '__main__':
    test0()
        
