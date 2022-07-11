#процедуры для использования в задачах на односвязный список в leetcode
class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

def getLinkedList(l):
    if l == []:
        return None

    head = ListNode(val=l[0])
    cur = head
    for it in l[1:]:
        cur.next = ListNode(it)
        cur = cur.next
    
    return head

def printLinkedList(l):
    while(l):
        print(l.val, end = ' ')
        l = l.next
    print('\n', end = '')
