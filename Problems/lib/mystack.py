#класс стек для задач из курса Хирьянова

class MyStack:
  def __init__(self):
    self.stack = []
    return

  def push(self,a):
    self.stack.append(a)
    return
  
  def pop(self):
    return self.stack.pop()
  
  def is_empty(self):
    return len(self.stack)==0

