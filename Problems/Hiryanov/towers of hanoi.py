#пример "ханойские башни"
#из лекции Хирьянова https://www.youtube.com/watch?v=0Bc8zLURY-c&list=PLRDzFCPr95fK7tr47883DFUbm4GeOjjc0&index=7

#простая реализация стека
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self,a):
        #для "ханойских башень" peek должен быть всегда больше значения a (для не пустого стека)
        assert self.peek() > a if not self.is_empty() else True, "запрещенное перемещение!"
        self.stack.append(a)
  
    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[len(self.stack)-1]
  
    def is_empty(self):
        return len(self.stack)==0

    def show(self):
        for i in self.stack:
            print(i, end=' ')
        print('')

class HanoiTowers:
    def __init__(self,n):
        self.towers = [MyStack(),MyStack(),MyStack()]
        for i in range(n,0,-1):
            self.towers[0].push(i)
        self.iters = 0
        self.size = n

    def elementary_move(self,start,finish):
        self.towers[finish].push(self.towers[start].pop())
        self.iters += 1


    def show(self):
        print("t0:", end = ' ')
        self.towers[0].show()

        print("t1:", end = ' ')
        self.towers[1].show()

        print("t2:", end = ' ')
        self.towers[2].show()

        print('')

    def move(self,start,finish,n):
        '''рекурсивно перемещает пирамиду длины n из стека start в стека finish'''

        #3-й номер стека, отличный от start и finish
        third_index = 3-start-finish
        if n == 1:
            self.elementary_move(start,finish)
            #показываем состояние стеков после элементарного перемещения
            self.show()
            return

        self.move(start,third_index,n-1)
        self.elementary_move(start,finish)
        #показываем состояние стеков после элементарного перемещения
        self.show()
        self.move(third_index,finish,n-1)

    def solve(self):
        self.show()
        self.move(0,2,self.size)
        print(f'number of elementary movements performed: {self.iters}')


if __name__ == '__main__':
    towers = HanoiTowers(3)
    towers.solve()
