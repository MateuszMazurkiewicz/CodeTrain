import unittest
from task import Solution

class TestBrackets(unittest.TestCase):
    def test_invalid(self):
        self.assertEqual(Solution().isValid("()(){(())"), False)

    def test_invalid_opening(self):
        self.assertEqual(Solution().isValid("("), False)

    def test_invalid_oclosing(self):
        self.assertEqual(Solution().isValid("]"), False)

    def test_empty(self):
        self.assertEqual(Solution().isValid(""), True)

    def test_valid(self):
        self.assertEqual(Solution().isValid("([{}])()"), True)

if __name__ == '__main__':
    unittest.main()