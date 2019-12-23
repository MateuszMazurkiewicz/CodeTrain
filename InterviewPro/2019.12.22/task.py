'''
Write a function that reverses the digits a 32-bit signed integer, x. Assume that the environment can only store integers within the 32-bit signed integer range, [-2^31, 2^31 - 1]. The function returns 0 when the reversed integer overflows.

Example:

Input: 123
Output: 321
'''



class Solution:
    max_value = 2**31 - 1
    min_value = -2**31

    def reverse(self, x):
        if x > self.max_value or x < self.min_value:
            return 0
        res = 0
        while x > 0:
            res *= 10
            res += x % 10
            x = x // 10

        return res
  

print(Solution().reverse(123))
# 321
print(Solution().reverse(2**31))
# 0