'''
Given a list, find the k-th largest element in the list.
Input: list = [3, 5, 2, 4, 6, 8], k = 3
Output: 5
Here is a starting point:
'''

import random

def findKthLargest(nums, k):
    # Fill this in.
    pivot = random.choice(nums)
    nums.remove(pivot)
    left = [num for num in nums if num <= pivot]    
    right = [num for num in nums if num > pivot]


    left_len = len(left)
    if left_len == k:
        return pivot
    if left_len > k:
        findKthLargest(left, k)
    if left_len < k:
       findKthLargest(right, k - left_len - 1)

print(findKthLargest([3, 5, 2, 4, 6, 8], 3))
# 5