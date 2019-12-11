'''
Given an array, nums, of n integers, find all unique triplets (three numbers, a, b, & c) in nums such that a + b + c = 0. Note that there may not be any triplets that sum to zero in nums, and that the triplets must not be duplicates.

Example:
Input: nums = [0, -1, 2, -3, 1]
Output: [0, -1, 1], [2, -3, 1]
Here's a starting point:
'''

class Solution(object):
    def threeSum(self, nums):        
        results = []
        n = len(nums)
        for i in range(n):
            for j in range(i + 1,n):
                for k in range(j + 1,n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        x = [nums[i], nums[j], nums[k]]
                        if not self.check_if_present(x, results):
                            results.append(x)
        return results

    def check_if_present(self, x, results):
        k = len(x)
        for r in results:
            counter = 0
            for n in x:
                if not n in r:
                    continue
                else:
                    counter += 1
            if counter == k:
                return True
        return False


# Test Program
nums = [1, -2, 1, 0, 5, -2, 1, 1]
print(Solution().threeSum(nums))
# [[-2, 1, 1]]