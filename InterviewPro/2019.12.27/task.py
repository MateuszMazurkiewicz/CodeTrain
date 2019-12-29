'''
Starting at index 0, for an element n at index i, you are allowed to jump at most n indexes ahead. 
Given a list of numbers, find the minimum number of jumps to reach the end of the list.

Example:

Input: [3, 2, 5, 1, 1, 9, 3, 4]
Output: 2

Explanation:

The minimum number of jumps to get to the end of the list is 2:
3 -> 5 -> 4

Here's a starting point:
'''

def jumpToEnd(nums):
    n = nums.pop(0)
    if n >= len(nums):
        return 1

    jumps = sum(nums)

    for i in range(n):
        jumps = min(jumps, jumpToEnd(nums[i:]))

    return 1 + jumps

print(jumpToEnd([3, 2, 5, 1, 1, 9, 3, 4]))
# 2