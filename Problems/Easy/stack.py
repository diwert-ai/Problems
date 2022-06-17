#простая реализация стека и проверка на задачке про скобки
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

def braces_check(s):
  st = MyStack()
  for c in s:
    if c not in '{[()]}':
      continue

    if c in '({[':
      st.push(c)
    else:
      assert c in ')}]', f"right brace expected: got {c}"
      
      if st.is_empty():
        return False
      
      left=st.pop()
      if (c == ')' and left != '(') or \
         (c == '}' and left != '{') or \
         (c == ']' and left != '['): 
         return False

    
  return st.is_empty()

def test0():
    s = ['{[[[[{[[()]]}]]]]}','[}]','[{]}','[[[[[','{{{{{asd{asd{99}}}}}}}',
         '[[ddd]][{((kdasd)(dajdak))[asdasd]{dasd}}]','[[ddd]][{(kdasd)(dajdak))[asdasd]{dasd}}]']
    for t in s:
        print(t,braces_check(t))

if __name__ == '__main__':
    test0()


