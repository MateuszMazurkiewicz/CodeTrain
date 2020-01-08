'''
You are given the root of a binary tree. 
Find the path between 2 nodes that maximizes the sum of all the nodes in the path, and return the sum. 
The path does not necessarily need to go through the root.
'''

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

max_value = None

def maxPathSum(root):
    max_path(root)
    return max_value


def max_path(node):
    if node.left is None and node.right is None:
        return node.val

    max_left = 0
    max_right = 0

    if not node.left is None:
        max_left = max_path(node.left)
    if not node.right is None:    
        max_right = max_path(node.right)

    sum_all = max_left + max_right + node.val

    global max_value

    max_value = sum_all if max_value is None or sum_all > max_value else max_value


    return max(max_left, max_right, 0) + node.val

    


# (* denotes the max path)
#       *10
#       /  \
#     *2   *10
#     / \     \
#   *20  1    -25
#             /  \
#            3    4
root = Node(10)
root.left = Node(2)
root.right = Node(10)
root.left.left = Node(20)
root.left.right = Node(1)
root.right.right = Node(-25)
root.right.right.left = Node(3)
root.right.right.right = Node(4)
print(maxPathSum(root))
# 42