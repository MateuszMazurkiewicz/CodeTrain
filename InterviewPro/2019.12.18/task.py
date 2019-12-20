'''
You are given a binary tree representation of an arithmetic expression. In this tree, each leaf is an integer value
and a non-leaf node is one of the four operations: '+', '-', '*', or '/'.

Write a function that takes this tree and evaluates the expression.

Example:

    *
   / \
  +    +
 / \  / \
3  2  4  5


This is a representation of the expression (3 + 2) * (4 + 5), and should return 45.

Here's a starting point:
'''

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

PLUS = "+"
MINUS = "-"
TIMES = "*"
DIVIDE = "/"


def evaluate(root):
    if root.val not in [PLUS, MINUS, TIMES, DIVIDE]:
        return root.val

    elif root.val == PLUS:
        return evaluate(root.right) + evaluate(root.left)
        
    elif root.val == MINUS:
        return evaluate(root.right) - evaluate(root.left)
    elif root.val == TIMES:
        return evaluate(root.right) * evaluate(root.left)
    elif root.val == DIVIDE:
        return evaluate(root.right) / evaluate(root.left)


tree = Node(TIMES)
tree.left = Node(PLUS)
tree.left.left = Node(3)
tree.left.right = Node(2)
tree.right = Node(PLUS)
tree.right.left = Node(4)
tree.right.right = Node(5)
print(evaluate(tree))
# 45