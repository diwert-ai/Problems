from lib.linkedlist import ListNode
from typing import Optional

def print_segment(prev:ListNode,lst:ListNode,post:ListNode):
    while(not (lst is post)):
        print(lst.val, end = ' ')
        lst = lst.next
    print('')

def getEndOfLinkedList(lst:ListNode) -> ListNode:
    while(lst.next):
        lst = lst.next
    return lst

def inverse_segment(prev:ListNode,lst:ListNode,post:ListNode):

    end = lst
    

    if post != None:
        while not (end.next is post):
            end = end.next
    else:
        while end.next != None:
            end = end.next

    end.next = None
       
    new_lst = inverseLinkedList(lst)

    if prev != None:
        prev.next = new_lst
           
    new_end = lst
    new_end.next = post

    if prev == None:
        return new_lst
    else:
        return None


def inverse_segment_i(lst:ListNode,left_bound_index:int,right_bound_index:int):
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
            
    
    return inverse_segment(prev,seg,post)

def inverseLinkedList(lst:ListNode, new_head:ListNode = None):

    end  = lst

    while end.next != None:
        prev = end
        end = end.next
    

    if new_head == None: 
        new_head = end
        
    end.next = prev
    prev.next = None

    if lst.next != None:
        return inverseLinkedList(lst,new_head)
    else:
        return new_head

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
            return inverseLinkedList(lst,new_head)
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


def test0():
    nums = [i for i in range(20)]
    a = 3
    b = 8
    print(nums)
    list1 = getLinkedList(nums)
    prev = list1
    for i in range(a):
        prev = prev.next
    print('prev ', a)

    lst = prev.next

    post = list1
    for i in range(b):
        post = post.next
    print('post ',b)

def test1():
    nums = [i for i in range(15)]
    lst = getLinkedList(nums)
    printLinkedList(lst)
    h = inverseLinkedList(lst)
    printLinkedList(h)

def test2():
    nums = [i for i in range(15)]
    list1 = getLinkedList(nums)
    printLinkedList(list1)
    
    a,b = 7,8
    prev,post = list1,list1

    for i in range(a):
        prev = prev.next

    if a < 0: 
        prev = None
        lst = list1
    else:
        lst = prev.next

    for i in range(b):
        post = post.next

    inverse_segment(prev,lst,post)

    printLinkedList(list1)

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    cur = head
    l = 0
    while(cur.next):
        cur = cur.next
        l += 1

    start = -1
    stop = start + k + 1

    while stop < l+2:
        #print(f'l={l} start={start} stop={stop}')
        n_head = inverse_segment_i(head,start,stop)
        head = n_head if n_head != None else head
        #printLinkedList(head)
        start = stop-1
        stop = start + k + 1

    return head

  


def test3():
    nums = [i for i in range(20)]
    
    lst = getLinkedList(nums)
    printLinkedList(lst)

    nlst = inverse_segment_i(lst,5,15)
    printLinkedList(nlst if nlst != None else lst)

def test4():
    nums = [i for i in range(20)]
    lst = getLinkedList(nums)
    printLinkedList(lst)

    nlst = reverseKGroup(lst,10)
    printLinkedList(nlst)

def test5():
    nums = [i+1 for i in range(5)]
    lst = getLinkedList(nums)
    printLinkedList(lst)

    printLinkedList(Solution().reverseKGroup(lst,3))

def test6():
    a = (10,11)
    print(a)



if __name__ == '__main__':
    test6()
