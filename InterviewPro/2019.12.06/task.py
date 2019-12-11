'''
You are given the root of a binary tree. Find and return the largest subtree of that tree, which is a valid binary search tree.

Here's a starting point:
'''

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

    def __str__(self):
        # preorder traversal
        answer = str(self.key)
        if self.left:
            answer += str(self.left)
        if self.right:
            answer += str(self.right)
        return answer

def largest_bst_subtree(root):
    # Fill this in.
    return check_tree(root)[1]


def check_tree(node):
    if not node:
        return 0, None, True

    left_ok = not node.left or node.left.key < node.key
    right_ok = not node.right or node.right.key > node.key
    is_correct_node = left_ok and right_ok

    left_size, left_node, left_correct_tree = check_tree(node.left)
    right_size, right_node, right_correct_tree = check_tree(node.right)

    if right_correct_tree and left_correct_tree and is_correct_node:
        return left_size + right_size + 1, node, True
    else:
        if left_size > right_size:
            return left_size, left_node, False
        else:
            return right_size, right_node, False



#         5
#        / \
#     6     7
#    /     / \
# 2     4     9
node = TreeNode(5)
node.left = TreeNode(6)
node.right = TreeNode(7)
node.left.left = TreeNode(2)
node.right.left = TreeNode(4)
node.right.right = TreeNode(9)
print(largest_bst_subtree(node))
#749