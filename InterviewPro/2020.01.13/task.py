'''
Given the root of a binary tree, print its level-order traversal. For example:

  1
 / \
2   3
   / \
  4   5


The following tree should output 1, 2, 3, 4, 5.
'''

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def print_level_order(root):
    level = [root]
    while level:
        tmp_level = []
        for x in level:
            if x.left:
                tmp_level.append(x.left)
            if x.right:
                tmp_level.append(x.right)

            print(x.val, end=' ')

        level = tmp_level

  # Fill this in.

root = Node(1, Node(2), Node(3, Node(4), Node(5)))
print_level_order(root)
# 1 2 3 4 5
