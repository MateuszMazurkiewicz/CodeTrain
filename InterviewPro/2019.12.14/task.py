'''
 are given an array of integers. Return an array of the same size where the element at each index is the product of all the elements in the original array except for the element at that index.

For example, an input of [1, 2, 3, 4, 5] should return [120, 60, 40, 30, 24].

You cannot use division in this problem.

Here's a start:
'''

def products(nums):
    full = 1
    for x in nums:
        full *= x

    res = []
    for x in nums:
        res.append(full//x)

    return res


print(products([1, 2, 3, 4, 5]))
# [120, 60, 40, 30, 24]