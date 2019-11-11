#Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.

#Example:

#Input: s = 7, nums = [2,3,1,2,4,3]
#Output: 2

#Explanation: the subarray [4,3] has the minimal length under the problem constraint.

#Here is the method signature:

class Solution:
    def minSubArrayLen(self, nums, s):
        start = 0
        length = len(nums)
        summ = 0
        indexes = None
        for i in range(len(nums)):
            summ += nums[i]

            while summ >= s:
                if i - start  + 1 < length:
                    length = i - start + 1
                    indexes = (start, i)
                summ -= nums[start]
                start += 1                

        return length, indexes 

print(Solution().minSubArrayLen([2, 3, 1, 2, 4, 3], 7))
# 2