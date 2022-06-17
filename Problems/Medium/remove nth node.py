#https://leetcode.com/problems/remove-nth-node-from-end-of-list/
#Given the head of a linked list, remove the nth node from the end of the list and return its head.

# Definition for singly-linked list.
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n <= 0:
            return head

        if head == None: 
            return None

        node_n = head
        h = {}
        sz=1
        

        while node_n.next:
            h[sz]=node_n
            sz+=1
            node_n = node_n.next
        
        h[sz]=node_n

        if n > sz:
            return None
        
        if n == 1 and sz == 1:
            return None
        else:
            if n == 1:
                h[sz-1].next=None
            elif n == sz:
                head = h[2]
            else:
                h[sz-n].next = h[sz-n+2]
                
        
        return head

def get_linked_list(l):
     n  = len(l)
     if n == 0: return None


     h = ListNode(val=l[0])
     c = h
     for i in range(1,n):
         c.next = ListNode(val=l[i])
         c = c.next
     
     return h

def get_list(l):
    r = []
    c = l
    while(c):
        r.append(c.val)
        c = c.next
    return r


def print_linked_list(l):
    c = l
    while (c):
        print (c.val,end = ' ')
        c = c.next

def test0 ():
    print_linked_list(get_linked_list([1,3,2,4,2,4]))

def test1 ():
    t = [1,4,3,2,3,3]
    r = get_list(get_linked_list(t))
    print (r)
    print (t == r)

def test2 ():
    s = Solution()
    l = [-1]
    n = -1
    linked_l = get_linked_list(l)
    r = s.removeNthFromEnd(linked_l,n)
    print(l)
    print(get_list(r))
  
    

if __name__ == '__main__':
    test0()
    test1()
    test2()
    
