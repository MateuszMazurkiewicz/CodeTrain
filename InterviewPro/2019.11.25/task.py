'''
You are given the root of a binary tree. Return the deepest node (the furthest node from the root).

Example:

    a
   / \
  b   c
 /
d

The deepest node in this tree is d at depth 3.

Here's a starting point:
'''

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __repr__(self):
    # string representation
        return self.val


def deepest(node):
    if node:
        l = deepest(node.left)
        r = deepest(node.right)
        depth = max(l[0], r[0])
        if depth == 0:
            return 1, node.val
        elif l[0] > r[0]:
            return 1 + depth, l[1]
        else:
            return 1 + depth, r[1]
        
    return 0, None



root = Node('a')
root.left = Node('b')
root.left.left = Node('d')
root.right = Node('c')

print(deepest(root))
# (d, 3)