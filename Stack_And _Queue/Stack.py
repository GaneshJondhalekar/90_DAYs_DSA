
from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()
    
    def push(self,val):
        self.stack.append(val)

    def pop(self):
        return self.stack.pop()

#showing data at top
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        return 'Empty stack'
    
    def is_empty(self):
        return len(self.stack)==0

s=Stack()
s.push(3)
s.push(31)
s.push(43)
print(s.pop())
print(s.peek())
print(s.is_empty())
        
