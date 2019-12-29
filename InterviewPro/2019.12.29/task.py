'''
A k-ary tree is a tree with k-children, and a tree is symmetrical if the data of the left side of the tree is the same as the right side of the tree.

Here's an example of a symmetrical k-ary tree.

        4
     /     \
    3        3
  / | \    / | \
9   4  1  1  4  9

Given a k-ary tree, figure out if the tree is symmetrical.

Here is a starting point:
'''

class Node():
  def __init__(self, value, children=[]):
    self.value = value
    self.children = children

def is_symmetric(root):
    nodes_level = []
    values_level = []

    for child in root.children:
        nodes_level.append(child)

    while nodes_level:
        values_level = [node.value for node in nodes_level]
        m = len(nodes_level) // 2
        for i in range(m):
            if values_level[i] != values_level[-1 - i]:
                return False

        new_level = []
        for node in nodes_level:
            for child in node.children:
                new_level.append(child)

        nodes_level = new_level

    return True


tree = Node(4)
tree.children = [Node(3), Node(3)]
tree.children[0].children = [Node(9), Node(4), Node(1)]
tree.children[1].children = [Node(1), Node(4), Node(9)]
print(is_symmetric(tree))
# True