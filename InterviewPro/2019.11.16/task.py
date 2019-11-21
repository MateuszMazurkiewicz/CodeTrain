'''
You are given an array of integers. Return the largest product that can be made by multiplying any 3 integers in the array.

Example:

[-4, -4, 2, 8] should return 128 as the largest product can be made by multiplying -4 * -4 * 8 = 128.

Here's a starting point:
'''

def maximum_product_of_three(lst):
    # Fill this in.
    lst.sort()
    return max(lst[0]*lst[1]*lst[-1], lst[-3]*lst[-2]*lst[-1] )

print(maximum_product_of_three([-4, -4, 2, 8]))

# 128
