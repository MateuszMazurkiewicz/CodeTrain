import unittest
from task import Solution

class TestPalindrome(unittest.TestCase):

    def test_odd(self):
        s = 'aaban'
        result = Solution().find_odd(2, s)
        self.assertEqual(result[0], 3)
    
    def test_odd_single(self):
        s = 'axbaa'
        result = Solution().find_odd(2, s)
        self.assertEqual(result[0], 1)

    def test_even(self):
        s = 'aaban'
        result = Solution().find_even(0, s)
        self.assertEqual(result[0], 2)
    
    def test_even_zero(self):
        s = 'axbaa'
        result = Solution().find_even(1, s)
        self.assertEqual(result[0], 0)

    def test_palindrome_basic(self):
        s = "tracecars"
        self.assertEqual(str(Solution().longestPalindrome(s)), "racecar")


if __name__ == '__main__':
    unittest.main()