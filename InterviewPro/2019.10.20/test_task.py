import unittest
from task import Solution

class TestIndices(unittest.TestCase):

    def test_basic(self):
        arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
        x = 2             
        self.assertListEqual([1, 4], Solution().getRange(arr, x))

    def test_one(self):
        arr = [1,3,3,5,7,8,9,9,9,15]
        x = 9             
        self.assertListEqual([6, 8], Solution().getRange(arr, x))

    def test_two(self):
        arr = [100, 150, 150, 153] 
        x = 150             
        self.assertListEqual([1, 2], Solution().getRange(arr, x))

    def test_three(self):
        arr = [1,2,3,4,5,6,10] 
        x = 9             
        self.assertListEqual([-1, -1], Solution().getRange(arr, x))    

if __name__ == '__main__':
    unittest.main()