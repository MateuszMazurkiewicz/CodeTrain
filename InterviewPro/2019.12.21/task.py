'''
Given a list of integers, return the bounds of the minimum range that must be sorted so that the whole list would be sorted.

Example:

Input: [1, 7, 9, 5, 7, 8, 10]
Output: (1, 5)

Explanation:
The numbers between index 1 and 5 are out of order and need to be sorted.

Here's your starting point:
'''

def findRange(nums):
    s = sorted(nums)
    start = -1
    end = -1
    for i in range(len(nums)):
        if s[i] != nums[i]:
            start = i
            break

    for i in range(len(nums) - 1, -1, -1):
        if s[i] != nums[i]:
            end = i
            break

    return start, end


print(findRange([1, 7, 9, 5, 7, 8, 10]))
# (1, 5)