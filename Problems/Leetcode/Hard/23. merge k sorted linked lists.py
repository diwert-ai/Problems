# https://leetcode.com/problems/merge-k-sorted-lists/
# You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from linkedlist import ListNode, getLinkedList, printLinkedList


class Solution:
    def __init__(self):
        self.head = None
        self.end = None
    
    # мое решение для двух списков
    def merge_two_lists_my(self, list1: ListNode, list2: ListNode) -> ListNode:
        def merge(l1, l2):
            if l1 is None:
                self.end.next = l2 
                return self.head
            
            if l2 is None:
                self.end.next = l1
                return self.head
            
            if l1.val > l2.val:
                self.end.next = l2
                self.end = l2
                merge(l1, l2.next)
            else:
                self.end.next = l1
                self.end = l1
                merge(l1.next, l2)
            
            return self.head
        
        if list1 is None:
            return list2
        
        if list2 is None:
            return list1
        
        if list1.val > list2.val:
            self.head = self.end = list2
            return merge(list1, list2.next)
        
        self.head = self.end = list1
        return merge(list1.next, list2)

    # решение most votes для двух списков
    # https://leetcode.com/problems/merge-two-sorted-lists/discuss/1826693/Python3-MERGING-Explained
    # Time: O(n)
    # Space: O(1)
    @staticmethod
    def merge_two_lists(list1: ListNode, list2: ListNode) -> ListNode:
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

    # brute force решение
    # Time complexity : O(kN) where k is the number of linked lists.
    # We can merge two sorted linked list in O(n) time where nn is the total number of nodes in two lists.
    # Space complexity : O(1)
    # We can merge two sorted linked list in O(1) space.
    def merge_k_lists_bf(self, lists: list[ListNode]):
        if not lists:
            return None
        
        res = lists[0]
        
        for cur_list in lists[1:]:
            if not cur_list:
                continue
            res = self.merge_two_lists(res, cur_list)
        
        return res
    
    # мое решение
    def do_reduce(self, lists):
        n = len(lists)
        if n < 2:
            return lists
        
        res = []

        i = 0
        for i in range(n//2):
            res.append(self.merge_two_lists(lists[2*i], lists[2*i+1]))
                       
        if 2*i+1 == n-2:
            res.append(lists[n-1])
        
        return res
    
    # мое решение - попарный мердж
    # Time complexity : O(N* log k) where k is the number of linked lists.
    # Space complexity : O(1) We can merge two sorted linked lists in O(1) space.
    def merge_k_lists(self, lists: list[ListNode]):
        if not lists:
            return None
        
        if len(lists) == 1:
            return lists[0]
            
        while len(lists) > 2:
            lists = self.do_reduce(lists)

        return self.merge_two_lists(lists[0], lists[1])
                       

# test case 132 of 133
def test0():
    tests = [[7], [49], [73], [58], [30], [72], [44], [78], [23], [9], [40], [65], [92],
             [42], [87], [3], [27], [29], [40], [12], [3], [69], [9], [57], [60], [33],
             [99], [78], [16], [35], [97], [26], [12], [67], [10], [33], [79], [49], [79],
             [21], [67], [72], [93], [36], [85], [45], [28], [91], [94], [57], [1], [53],
             [8], [44], [68], [90], [24], [96], [30], [3], [22], [66], [49], [24], [1]]
    lists = []
    for test in tests:
        lists.append(getLinkedList(test))
    printLinkedList(Solution().merge_k_lists(lists))


if __name__ == '__main__':
    test0()
