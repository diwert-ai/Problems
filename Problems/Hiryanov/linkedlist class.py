#связный список
#из лекции Хирьянова - https://www.youtube.com/watch?v=Y4ithGiEO08&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=17

class LinkedList:
    def __init__(self, l = None):
        self._begin = None
        if l is not None:
            for x in l:
                self.insert(x)

    def insert(self,x):
        self._begin = [x,self._begin]

    def pop(self):
        assert self._begin is not None, "List is empty"
        x = self._begin[0]
        self._begin = self._begin[1]
        return x

    def print(self):
        cur = self._begin
        while cur is not None:
            print(cur[0], end=' ')
            cur = cur[1]
        print('')

def test0():
    a = LinkedList([6,7])
    a.insert(5)
    a.insert(10)
    a.print()
    print('pop:',a.pop())
    print('pop:',a.pop())
    a.print()
    a.pop()
    a.pop()
    a.print()
    
if __name__ == '__main__':
    test0()

