from collections import deque

class Queue:
    def __init__(self):
        self.queue=deque()

    def enqueue(self,val):
        self.queue.append(val)
    
    def dequeue(self):
        return self.queue.popleft()

    def peek(self):
        if not self.is_empty():
            return self.queue[0]
        return 'Empty queue'
    
    def is_empty(self):
        return len(self.queue)==0

q=Queue()
q.enqueue(22)
q.enqueue(93)
q.enqueue(87)
print(q.dequeue())
print(q.peek())
print(q.dequeue())
print(q.peek())
print(q.is_empty())
print(q.dequeue())
print(q.peek())
