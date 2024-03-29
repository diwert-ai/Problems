# процедуры для использования в задачах на односвязный список в leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def getLinkedList(lst):
    if not lst:
        return None

    head = ListNode(val=lst[0])
    cur = head
    for it in lst[1:]:
        cur.next = ListNode(it)
        cur = cur.next

    return head


def printLinkedList(lst):
    while lst:
        print(lst.val, end=' ')
        lst = lst.next
    print('\n', end='')
