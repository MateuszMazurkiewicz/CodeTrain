# Implement a class for a stack that supports all the regular functions (push, pop) and an additional function of max() 
# which returns the maximum element in the stack (return None if the stack is empty). 
# Each method should run in constant time.

class MaxStack:
  def __init__(self):
    # Fill this in.
    self.stack = []
    self.max_stack  = []

  def push(self, val):
    # Fill this in.
    self.stack.append(val)
    if len(self.max_stack) == 0 or self.max_stack[-1] < val:
        self.max_stack.append(val)
    else:
        self.max_stack.append(self.max_stack[-1])

  def pop(self):
    # Fill this in.
    self.stack.pop()
    self.max_stack.pop()

  def max(self):
    # Fill this in.
    return self.max_stack[-1]

s = MaxStack()
s.push(1)
s.push(2)
s.push(3)
s.push(2)
print(s.max())
# 3
s.pop()
s.pop()
print(s.max())
# 2