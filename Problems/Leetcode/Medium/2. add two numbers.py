# https://leetcode.com/problems/add-two-numbers/
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


from linkedlist import ListNode, getLinkedList, printLinkedList
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    # мое решение
    @staticmethod
    def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:
        
        pl1 = [l1.val]
        pl2 = [l2.val]
        
        p_next = l1.next
        while p_next is not None:
            pl1.append(p_next.val)
            p_next = p_next.next
        
        p_next = l2.next
        while p_next is not None:
            pl2.append(p_next.val)
            p_next = p_next.next
                            
        res = []
        len1 = len(pl1)
        len2 = len(pl2)
        
        if len1 != len2:
            if len1 > len2:
                for i in range(len1-len2):
                    pl2.append(0)
            else:
                for i in range(len2-len1):
                    pl1.append(0)
                len1 = len2

        s = pl1[0]+pl2[0]
        transit = (s - s % 10)//10
        ln = ListNode(s % 10)
        cur = ln
        for i in range(1, len1):
            s = pl1[i]+pl2[i]+transit
            transit = (s - s % 10)//10
            res.append(s % 10)
            cur.next = ListNode(s % 10)
            cur = cur.next
        
        if transit > 0:
            cur.next = ListNode(transit)
                    
        return ln


def test0():
    list1 = getLinkedList([1, 2, 3, 4, 5])
    list2 = getLinkedList([3, 4, 2, 3, 2, 9, 9, 9, 9])
    list3 = Solution.add_two_numbers(list1, list2)
    printLinkedList(list3)


if __name__ == '__main__':
    test0()
