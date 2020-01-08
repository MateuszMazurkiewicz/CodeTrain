'''
Given a sorted list of positive numbers, find the smallest positive number that cannot be a sum of any subset in the list.

Example:
Input: [1, 2, 3, 8, 9, 10]
Output: 7
Numbers 1 to 6 can all be summed by a subset of the list of numbers, but 7 cannot.
'''


def findSmallest(nums):
    sums = {}
    for i in range(len(nums) + 1):
        x = check_range(i, nums, sums)
        if not x is None:
            return x

def check_range(k, nums, sums):
    range_to_check = []
    if k == 0:
        range_to_check = list(range(1, nums[k] + 1))
    elif k < len(nums):
        range_to_check = list(range(nums[k - 1] + 1, nums[k] + 1))
    else:
        range_to_check = list(range(nums[k - 1] + 1, sum(nums) + 2))
    
    if k < len(nums):

        v = nums[k]

        if (v, ) not in sums:
            update_sums_new(v, sums)
        else:
            update_sums_existing(v, sums)

    computed = set(sums.values())

    for x in range_to_check:        
        if x not in computed:
            return x

    return None        

def update_sums_new(v, sums):
    new_sums = {}
    for key in sums.keys():
        tmp = sums[key] + v
        new_sums[key + (v,)] = tmp

    sums[(v,)] = v
    sums.update(new_sums)

def update_sums_existing(v, sums):
    for key in sums.keys():
        if v in key:
            tmp = sums[key] + v
            sums[key + (v,)] = tmp


print(findSmallest([1, 2, 3, 8, 9, 10]))
# 7
print(findSmallest([1, 2, 3, 4]))
# 11