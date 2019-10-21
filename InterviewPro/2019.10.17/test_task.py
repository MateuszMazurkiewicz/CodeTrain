import unittest
from task import Solution

class TestLengthOfLongestSubstring(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'), 10)

    def test_same(self):
         self.assertEqual(Solution().lengthOfLongestSubstring('aaaa'), 1)

    def test_two(self):
         self.assertEqual(Solution().lengthOfLongestSubstring('ax'), 2)

    def test_mixed(self):
         self.assertEqual(Solution().lengthOfLongestSubstring('aaaabc'), 3)

if __name__ == '__main__':
    unittest.main()