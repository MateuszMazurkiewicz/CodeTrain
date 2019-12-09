'''
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library’s sort function for this problem.

Can you do this in a single pass?

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

Here's a starting point:
'''

class Solution:
    def sortColors(self, nums):
        zero_index = 0
        two_index = len(nums) - 1
        
        while nums[zero_index] == 0:
            zero_index += 1
        
        while nums[two_index] == 2:
            two_index -= 1

        index = zero_index

        while index < len(nums) and index <= two_index:            
            while nums[index] == 2 or nums[index] == 0:
                if nums[index] == 2:
                    nums[index] = nums[two_index]
                    nums[two_index] = 2
                    two_index -= 1

                if nums[index] == 0:
                    nums[index] = nums[zero_index]
                    nums[zero_index] = 0
                    zero_index += 1

            index += 1

nums = [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]
print("Before Sort: ")
print(nums)
# [0, 1, 2, 2, 1, 1, 2, 2, 0, 0, 0, 0, 2, 1]

Solution().sortColors(nums)
print("After Sort: ")
print(nums)
# [0, 0, 0, 0, 0, 1, 1, 1, 1, 2, 2, 2, 2, 2]