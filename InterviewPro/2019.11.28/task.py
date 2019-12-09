'''
You are given the root of a binary search tree. Return true if it is a valid binary search tree, and false otherwise. Recall that a binary search tree has the property that all values in the left subtree are less than or equal to the root, and all values in the right subtree are greater than or equal to the root.

Here's a starting point:
'''

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_bst(root):
    stack = []
    stack.append(root)

    while stack:
        tmp_node = stack.pop()
        if not children_valid(tmp_node):
            return False

        if tmp_node.right:
            stack.append(tmp_node.right)

        if tmp_node.left:
            stack.append(tmp_node.left)

    return True


def children_valid(node):
    return (node.left is None or node.left.key <= node.key) and (node.right is None or node.right.key > node.key)




a = TreeNode(5)
a.left = TreeNode(3)
a.right = TreeNode(7)
a.left.left = TreeNode(1)
a.left.right = TreeNode(4)
a.right.left = TreeNode(6)
print(is_bst(a))

#    5
#   / \
#  3   7
# / \ /
#1  4 6