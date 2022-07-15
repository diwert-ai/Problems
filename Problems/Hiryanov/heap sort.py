'''
структра данных heap (куча или пирамида) и сортировка массива
из курса Тимофея Хирьянова: https://www.youtube.com/watch?v=XwNfhI8498k

1.Элементы массива отображаются в бинарное дерево, так что
  потомки i-го элемента массива имеют номера 2*i+1 и 2*i+2 в массиве. 
  Т.о. элемент с индексом 0 является корнем.
2.Потомки либо всегда не меньше (и тогда в корне минимум) своего родителя
  либо всегда не больше (и тода в корне максимум).
3.Глубина листьев оличается не более чем на 1.
4.Уровни заполняются без пропусков. 
'''

class Heap:
    def __init__(self):
        self.values =  []
        self.size = 0

    #поднять элемент c i го места вверх по дереву так чтобы стуктура стала кучей
    #вызывается при добавлении нового элемента
    #O(log(size)) - операций
    def sift_up(self,i):
        while i!=0 and self.values[i]<self.values[(i-1)//2]:
            self.values[i],self.values[(i-1)//2] = self.values[(i-1)//2],self.values[i]
            i = (i-1)//2
    
    #спустить i-й элемент вниз так чтобы структура стала кучей
    #вызывается после экстракции минимума (максимума) из корня, на место которого 
    #перемещается последний элемент,а затем спускается на правильную позицию
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

    #добавляем новый элемент в конец
    #затем поднимаем его по дереву (куче) на
    #правильную позицию
    #O(log(size)) - операций
    def insert(self,a):
        self.values.append(a)
        self.size+=1
        self.sift_up(self.size-1)
            
    #извлекаем корень (минимальный либо максимальный элемент)
    #кладем на его место последний элемент и спускаем его на
    #правильную позицию в дереве (куче)
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

#трансформация массива в кучу
#O(size*log(size)) - операций
def heapify(a:list):
    h = Heap()

    for i in a:
        h.insert(i)

    return h

#быстрая транформация массива в кучу
#O(size) - операций
def fast_heapify(a: list):
    h = Heap()

    #h.values ссылается на копию 'a' (не на 'a', а именно на копию) 
    h.values = a[:]
    h.size = len(a)

    #первую половину элементов поочередно 
    #(в обратном порядке) спускаем по дереву
    #этого достаточно для формирования кучи
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
    print('naive heapify')
    t = [9,2,1,2,4,7,3,2,0]
    print(t)
    h = heapify(t)
    s = get_sorted_arr(h)
    print(s)
    print(sorted(t)==s)

def test2():
    print('fast heapify')
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





  
