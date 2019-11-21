'''
Implement a queue class using two stacks. A queue is a data structure that supports the FIFO protocol (First in = first out). Your class should support the enqueue and dequeue methods like a standard queue.

Here's a starting point:
'''

class Queue:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []    
    
    def enqueue(self, val):
        self.stack_1.append(val)
    


    def dequeue(self):
        while len(self.stack_1) > 0:
            self.stack_2.append(self.stack_1.pop())

        res = self.stack_2.pop()
        while len(self.stack_2) > 0:
            self.stack_1.append(self.stack_2.pop())
        return res


   

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
# 1 2 3