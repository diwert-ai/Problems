#структра данных heap (куча или пирамида) и сортировка массива
#из курса Тимофея Хирьянова: https://www.youtube.com/watch?v=XwNfhI8498k


class Heap:
    def __init__(self):
        self.values =  []
        self.size = 0

    def sift_up(self,i):
        while i!=0 and self.values[i]<self.values[(i-1)//2]:
            self.values[i],self.values[(i-1)//2] = self.values[(i-1)//2],self.values[i]
            i = (i-1)//2


    def sift_down(self,i):
        pass

    def insert(self,a):
        self.values.append(a)
        self.size+=1
        self.sift_up(self.size-1)
            
            
    def extract_min(self):
        m = self.values[0]
        self.values[0] = self.values.pop()
        self.size-=1
        self.sift_down(0)

        return m
       

h = Heap()
h.insert(0)
h.insert(1)
h.insert(-1)
h.insert(-10)
h.insert(-20)
h.insert(-40)

print(h.values)
print(h.extract_min())
print(h.values)


  
