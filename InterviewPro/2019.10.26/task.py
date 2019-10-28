# Given an integer k and a binary search tree, find the floor (less than or equal to) of k, and the ceiling (larger than or equal to) of k. If either does not exist, then print them as None.

# Here is the definition of a node for the tree.

class Node:
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

def findCeilingFloor(root_node, k, floor=None, ceil=None):
  # Fill this in.

    if root_node is None:
        return (floor, ceil)

    tmp = Node(root_node.value)
    tmp.left = root_node.left
    tmp.right = root_node.right

    while tmp is not None:
        if tmp.value == k:
            floor = k

        if tmp.value > k:
            tmp = tmp.left
        else:
            floor = tmp.value
            tmp = tmp.right

    tmp = Node(root_node.value)
    tmp.left = root_node.left
    tmp.right = root_node.right

    while tmp is not None:
        if tmp.value == k:
            ceil = k
        if tmp.value > k:
            ceil = tmp.value
            tmp = tmp.left            
        else:            
            tmp = tmp.right

    return (floor, ceil)

root = Node(8) 
root.left = Node(4) 
root.right = Node(12) 
  
root.left.left = Node(2) 
root.left.right = Node(6) 
  
root.right.left = Node(10) 
root.right.right = Node(14) 

print(findCeilingFloor(root, 5))
# (4, 6)