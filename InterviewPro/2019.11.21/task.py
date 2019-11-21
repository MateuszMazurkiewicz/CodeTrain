'''
You are given an array of k sorted singly linked lists. Merge the linked lists into a single sorted linked list and return it.

Here's your starting point:
'''

class Node(object):
  def __init__(self, val, next=None):
    self.val = val
    self.next = next

  def __str__(self):
    c = self
    answer = ""
    while c:
      answer += str(c.val) if c.val else ""
      c = c.next
    return answer

def merge(lists):
    res = None
    current = None
    while True:
        if len(lists) == 0:
            break        

        index = 0
        minimal = lists[0].val
        for i in range(len(lists)):
            if lists[i].val < minimal:
                minimal = lists[i].val
                index = i
        if res == None:
            res = lists[ index]
            current = res
            lists[index] = lists[ index].next
        else:
            current.next = lists[index]
            current = current.next
            lists[index] = lists[index].next

        if lists[index] is None:
            lists.pop(index)

    return res


a = Node(1, Node(3, Node(5)))
b = Node(2, Node(4, Node(6)))
c = Node(2, Node(7, Node(8)))
print(merge([a, b, c]))
# 122345678