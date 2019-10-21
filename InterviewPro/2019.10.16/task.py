#Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#Output: 7 -> 0 -> 8
#Explanation: 342 + 465 = 807.

#Here is the function signature as a starting point (in Python):

# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0):
    # Fill this in.
    current_l1 = l1
    current_l2 = l2  
    is_over_ten = 0
    result = None
    tmp = None

    while current_l1 or current_l2:
        val_l1 = 0
        val_l2 = 0

        if current_l1:
            val_l1 = current_l1.val

        if current_l2:
            val_l2 = current_l2.val

        tmp_sum = val_l1 + val_l2 + is_over_ten 

        if not result:
            result = ListNode(tmp_sum % 10)
            tmp = result
        else:
            tmp.next = ListNode(tmp_sum % 10)
            tmp = tmp.next

        if tmp_sum >= 10:
            is_over_ten = 1

        if current_l1:
            current_l1 = current_l1.next

        if current_l2:
            current_l2 = current_l2.next  

    return result

l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)

result = Solution().addTwoNumbers(l1, l2)
while result:
  print(result.val, end=' ')
  result = result.next
# 7 0 8