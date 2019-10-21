import unittest
from task import Solution
from task import ListNode

class TestAdd(unittest.TestCase):

    def test_basic(self):
        l1 = ListNode(2)
        l1.next = ListNode(4)
        l1.next.next = ListNode(3)

        l2 = ListNode(5)
        l2.next = ListNode(6)
        l2.next.next = ListNode(4)

        result = Solution().addTwoNumbers(l1, l2)
        test_list = []

        while result:
            test_list.append(result.val)
            result = result.next
        
        self.assertListEqual(test_list, [7, 0, 8])

if __name__ == '__main__':
    unittest.main()