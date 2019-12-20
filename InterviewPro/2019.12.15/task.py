'''
Given two arrays, write a function to compute their intersection - the intersection means the numbers that are in both arrays.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]

Note:
Each element in the result must be unique.
The result can be in any order.

Here's a starting point:
'''

class Solution:
    def intersection(self, nums1, nums2):
        s1 = set(nums1)
        s2 = set(nums2)
        return list(s1.intersection(s2))

    def in_list(self, x, l):
        for i in l:
            if x == i:
                return True

        return False


    def intersection_slow(self, nums1, nums2):
        res = []

        for x in nums1:
            for y in nums2:
                if x == y and not self.in_list(x, res):
                    res.append(x)

        return res


print(Solution().intersection([4, 9, 5], [9, 4, 9, 8, 4]))

print(Solution().intersection_slow([4, 9, 5], [9, 4, 9, 8, 4]))

# [9, 4]