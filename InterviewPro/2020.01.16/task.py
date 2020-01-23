'''
You are given the root of a binary tree. Find the level for the binary tree with the minimum sum, and return that value.

For instance, in the example below, the sums of the trees are 10, 2 + 8 = 10, and 4 + 1 + 2 = 7. So, the answer here should be 7.
'''

class Node:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

def minimum_level_sum(root):
    level = [root]
    min_sum = root.val

    while level:
        tmp_level = []
        for node in level:            
            if node.left:
                tmp_level.append(node.left)

            if node.right:
                tmp_level.append(node.right)

        level = tmp_level
        if level:
            tmp_sum = 0
            for x in level:
                tmp_sum += x.val
            min_sum = min(min_sum, tmp_sum)

    return min_sum


#     10
#    /  \
#   2    8
#  / \    \
# 4   1    2
node = Node(10)
node.left = Node(2)
node.right = Node(8)
node.left.left = Node(4)
node.left.right = Node(1)
node.right.right = Node(2)

print(minimum_level_sum(node))