import unittest
from task import ListNode

class ReverseTest(unittest.TestCase):

    def test_loop(self):
        testHead = ListNode(4)
        node1 = ListNode(3)
        testHead.next = node1
        node2 = ListNode(2)
        node1.next = node2
        node3 = ListNode(1)
        node2.next = node3
        testTail = ListNode(0)
        node3.next = testTail
        
        testHead.reverseIteratively(testHead)
        self.assertListEqual(testTail.toList(), [0, 1, 2, 3, 4])

    def test_recursive(self):
        testHead = ListNode(4)
        node1 = ListNode(3)
        testHead.next = node1
        node2 = ListNode(2)
        node1.next = node2
        node3 = ListNode(1)
        node2.next = node3
        testTail = ListNode(0)
        node3.next = testTail
        
        testHead.reverseRecursively(testHead)
        self.assertListEqual(testTail.toList(), [0, 1, 2, 3, 4])

if __name__ == '__main__':
    unittest.main()