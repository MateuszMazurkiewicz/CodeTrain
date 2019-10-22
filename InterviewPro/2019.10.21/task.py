#Given a singly-linked list, reverse the list. This can be done iteratively or recursively. Can you get both solutions?

#Example:

#Input: 4 -> 3 -> 2 -> 1 -> 0 -> NULL
#Output: 0 -> 1 -> 2 -> 3 -> 4 -> NULL

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
  
  # Function to print the list
    def printList(self):
        node = self
        output = '' 
        while node != None:
            output += str(node.val)
            output += " "
            node = node.next
        print(output)

    def toList(self):
        res = []
        node = self        
        while node != None:
            res.append(node.val)     
            node = node.next

        return res

  # Iterative Solution
    def reverseIteratively(self, head):
    # Implement this.
        if head is None or head.next is None:
            return head

        current = head.next 
        head.next = None 

        while current:
            next_node = current.next
            current.next = head
            head = current
            current = next_node 


  # Recursive Solution  
    def reverseRecursively(self, head):
    # Implement this.  
        def reverse(head, current):
            if current is None:
                return

            next_node = current.next
            current.next = head
            head = current
            current = next_node

            reverse(head, current)  

        if head is None or head.next is None:
            return

        current = head.next
        head.next = None

        reverse(head, current)


# Test Program
# Initialize the test list: 
testHead = ListNode(4)
node1 = ListNode(3)
testHead.next = node1
node2 = ListNode(2)
node1.next = node2
node3 = ListNode(1)
node2.next = node3
testTail = ListNode(0)
node3.next = testTail

print("Initial list: ")
testHead.printList()
# 4 3 2 1 0
#testHead.reverseIteratively(testHead)
testHead.reverseRecursively(testHead)
#print("List after reversal: ")
testTail.printList()

# 0 1 2 3 4