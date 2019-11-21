'''
You are given an array of integers. Find the maximum sum of all possible contiguous subarrays of the array.

Example:

[34, -50, 42, 14, -5, 86]

Given this input array, the output should be 137. The contiguous subarray with the largest sum is [42, 14, -5, 86].

Your solution should run in linear time.

Here's a starting point:
'''

def max_subarray_sum(arr):
    max_sum = arr[0]
    tmp_sum = arr[0]

    for i in range(1, len(arr)):
        tmp_sum += arr[i]
        if tmp_sum > max_sum:
            max_sum = tmp_sum
        if arr[i] > tmp_sum:
            tmp_sum = arr[i]

    return max_sum

print(max_subarray_sum([34, -50, 42, 14, -5, 86]))
# 137