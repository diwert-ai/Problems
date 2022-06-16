#структра данных heap (куча или пирамида) и сортировка массива
#из курса Тимофея Хирьянова: https://www.youtube.com/watch?v=XwNfhI8498k


class Heap:
    def __init__(self):
        self.heap =  []
        self.sz = 0

    def add(self,a):
        self.heap.append(a)
        self.sz+=1
        if self.sz == 1: return

        p_index = (self.sz-2)//2
        a_index = self.sz-1
        

        while (p_index>=0):
            p = self.heap[p_index]
            if a>=p: return
            self.heap[a_index],self.heap[p_index] = p,a
            a_index, p_index = p_index,(p_index-1)//2
            
            
    def del_element(self,i):
        pass

h = Heap()
h.add(4)
h.add(5)
h.add(2)
h.add(5)
h.add(8)
h.add(1)
h.add(-1)
h.add(10)
h.add(2)
h.add(20)
h.add(-100)


print(h.heap)

  
