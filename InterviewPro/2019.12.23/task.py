'''
Design a simple stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Note: be sure that pop() and top() handle being called on an empty stack.
'''

class minStack(object):
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, x):
        self.stack.append(x)
        if len(self.min_stack) == 0 or self.min_stack[-1] > x:
            self.min_stack.append(x)
        else:
            self.min_stack.append(self.min_stack[-1])

    def pop(self):
        self.min_stack.pop()
        return self.stack.pop()

    def top(self):
    # Fill this in.
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

x = minStack()
x.push(-2)
x.push(0)
x.push(-3)
print(x.getMin())
# -3
x.pop()
print(x.top())
# 0
print(x.getMin())
# -2