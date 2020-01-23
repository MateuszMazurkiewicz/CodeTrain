'''
Given a non-empty array where each element represents a digit of a non-negative integer, add one to the integer. The most significant digit is at the front of the array and each element in the array contains only one digit. Furthermore, the integer does not have leading zeros, except in the case of the number '0'.

Example:

Input: [2,3,4]
Output: [2,3,5]
'''

class Solution():
    def plusOne(self, digits):
        current_index = -1
        to_add = 1

        while to_add:
            if current_index == -1 * len(digits) - 1:
                digits.insert(0, 0)
                current_index = -1 * len(digits)

            digits[current_index] = (digits[current_index] + 1) % 10

            if digits[current_index] == 0:
                to_add = 1
                current_index -= 1
                
            else:
                to_add = 0

            

        return digits


num = [2, 9, 9]
print(Solution().plusOne(num))
# [3, 0, 0]

num = [9, 9, 9]
print(Solution().plusOne(num))