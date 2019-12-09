'''
You are given an array of integers. Return the smallest positive integer that is not present in the array. The array may contain duplicate entries.

For example, the input [3, 4, -1, 1] should return 2 because it is the smallest positive integer that doesn't exist in the array.

Your solution should run in linear time and use constant space.

Here's your starting point:
'''

def first_missing_positive(nums):
    if min(nums) > 1:
        return 1

    one_greater = set()

    for num in nums:
        if num <= 0:
            continue
        if (num + 1) not in one_greater:
            one_greater.add(num + 1)

    
    for num in nums:
        if num in one_greater:
            one_greater.remove(num)

    return min(one_greater)
    


print(first_missing_positive([3, 4, -1, 1]))
# 2

