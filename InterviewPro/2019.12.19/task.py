'''
Daily Interview Pro
Hi, here's your problem today. This problem was recently asked by Apple:

You are given the root of a binary tree. You need to implement 2 functions:

1. serialize(root) which serializes the tree into a string representation
2. deserialize(s) which deserializes the string back to the original tree that it represents

For this problem, often you will be asked to design your own serialization format. However, for simplicity, let's use the pre-order traversal of the tree. Here's your starting point:
'''

class Node:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def __str__(self):
    # pre-order printing of the tree.
    result = ''
    result += str(self.val)
    if self.left:
      result += str(self.left)
    if self.right:
      result += str(self.right)
    return result

def serialize(root):
    result = ''
    result += str(root.val) + ' '
    if root.left:
        result += serialize(root.left)
    else:
        result += '# '
    if root.right:
        result += serialize(root.right)
    else:
        result += '# '
    return result

def deserialize(data):
    return help(data.split(' '))

def help(list_data):
    if list_data[0] == '#':
        list_data.pop(0)
        return None

    
    node = Node(int(list_data.pop(0)))
    

    node.left = help(list_data)

    node.right = help(list_data)

    return node


    

#     1
#    / \
#   3   4
#  / \   \
# 2   5   7
tree = Node(1)
tree.left = Node(3)
tree.left.left = Node(2)
tree.left.right = Node(5)
tree.right = Node(4)
tree.right.right = Node(7)

print(serialize(tree))
# 1 3 2 # # 5 # # 4 # 7 # #
print(deserialize('1 3 2 # # 5 # # 4 # 7 # #'))
# 132547