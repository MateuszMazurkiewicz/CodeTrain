'''
Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
You must do this in-place without making a copy of the array.
Minimize the total number of operations.

Here is a starting point:
'''

class Solution:
    def moveZeros(self, nums):
        last = len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 0  and last > i:
                for j in range(i, last):
                    self.swap(j, j + 1, nums)
                last -= 1

    def swap(self, a, b, array):
        tmp = array[a]
        array[a] = array[b]
        array[b] = tmp

nums = [0, 0, 0, 2, 0, 1, 3, 4, 0, 0]
Solution().moveZeros(nums)
print(nums)
# [2, 1, 3, 4, 0, 0, 0, 0, 0, 0]