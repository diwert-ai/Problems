#структра данных heap (куча или пирамида) и сортировка массива
#из курса Тимофея Хирьянова: https://www.youtube.com/watch?v=XwNfhI8498k

class Heap:
    def __init__(self):
        self.values =  []
        self.size = 0

    #O(log(size)) - операций
    def sift_up(self,i):
        while i!=0 and self.values[i]<self.values[(i-1)//2]:
            self.values[i],self.values[(i-1)//2] = self.values[(i-1)//2],self.values[i]
            i = (i-1)//2

    #O(log(size)) - операций
    def sift_down(self,i):
        while 2*i + 1 < self.size:
            j = i

            if self.values[i] > self.values[2*i+1]:
                j = 2*i + 1

            if 2*i + 2 < self.size and self.values[j] > self.values[2*i+2]:
                j = 2*i + 2

            if i == j:
                break

            self.values[i],self.values[j] = self.values[j],self.values[i]
            i = j

    #O(log(size)) - операций
    def insert(self,a):
        self.values.append(a)
        self.size+=1
        self.sift_up(self.size-1)
            
    #O(log(size)) - операций        
    def extract_min(self):
        if self.size == 0:
            return None

        m = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size-=1
        self.sift_down(0)

        return m

#O(size*log(size)) - операций
def heapify(a):
    h = Heap()

    for i in a:
        h.insert(i)

    return h

#O(size) - операций
def fast_heapify(a):
    h = Heap()

    h.values = a[:]
    h.size = len(a)

    for i in reversed(range(len(a)//2)):
        h.sift_down(i)

    return h

#О(size*log(size)) - операций
def get_sorted_arr(h):
    r = []

    for i in range(h.size):
        r.append(h.extract_min())

    return r

       
def test0():
    h = Heap()
    t = [0,2,3,2,1,2,4,3,2,4,6,8,9,7,6,8,6,5,3,2,3,4,5,-1]
    s = []
    for i in t:
        h.insert(i)

    print(h.values)
    for i in range(h.size):
        s.append(h.extract_min())
    print(s)
    print(sorted(t)==s)

def test1():
    t = [9,2,1,2,4,7,3,2,0]
    print(t)
    h = heapify(t)
    s = get_sorted_arr(h)
    print(s)
    print(sorted(t)==s)

def test2():
    t = [9,2,1,2,4,7,3,2,0]
    print(t)
    h = fast_heapify(t)
    s = get_sorted_arr(h)
    print(s)
    print(sorted(t)==s)

if __name__ == '__main__':
    test0()
    test1()
    test2()





  
