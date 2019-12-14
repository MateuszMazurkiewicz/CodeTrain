'''
Given a sorted list of numbers, return a list of strings that represent all of the consecutive numbers.

Example:

Input: [0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]
Output: ['0->2', '5->5', '7->11', '15->15']

Assume that all numbers will be greater than or equal to 0, and each element can repeat.

Here is a starting point:
'''

def findRanges(nums):
    res = []
    start = nums[0]
    end = nums[0]
    for i in range(1, len(nums)):
        current = nums[i]
        if current == end:
            continue
        elif current == end + 1:
            end += 1
        else:
            res.append(f'{start}->{end}')
            start = nums[i]
            end = nums[i]

    res.append(f'{start}->{end}')
    return res



print(findRanges([0, 1, 2, 5, 7, 8, 9, 9, 10, 11, 15]))
# ['0->2', '5->5', '7->11', '15->15']