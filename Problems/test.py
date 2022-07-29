from collections import deque

class Test:
    def __init__(self):
        self.field = 10


class TestSet:
    def __init__(self):
        self.tests = []
        pass


    def add_tests(self, testType, num_tests):
        self.tests += [testType()] * num_tests

t1 = Test()
t2 = []
print(t1.field)
ts = TestSet()
ts.add_tests(Test, 10)
for test in ts.tests:
    print(test.field)

class arm:
    def __init__(self, l=[1,2,3,4]):
        self.units = deque(l)

    def reset(self):
        new_q = deque()
        while self.units:
            r = self.units.popleft()
            new_q.append(r*10)
        self.units = new_q


a1 = [1,2,3]
a2 = [6]
print(deque([a1[0]])+  deque(a2) + deque(a1[1:]))



