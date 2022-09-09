# класс стек для задач из курса Хирьянова

class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, a):
        self.stack.append(a)

    def pop(self):
        return self.stack.pop() if self.stack else None

    def is_empty(self):
        return len(self.stack) == 0

    def peak(self):
        size = len(self.stack)
        return self.stack[size-1] if size else None
