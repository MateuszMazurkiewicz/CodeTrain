'''
Given a list of numbers of size n, where n is greater than 3, find the maximum and minimum of the list using less than 2 * (n - 1) comparisons.

Here's a start:
'''

def find_min_max(nums):
    min_val = nums[0]
    max_val = nums[0]

    for i in range(1, len(nums)):
        current = nums[i]
        max_val =  current if current > max_val else max_val

        min_val =  current if current < min_val else min_val

    return min_val, max_val



print(find_min_max([3, 5, 1, 2, 4, 8]))
# (1, 8)