'''
You are given an array of integers. Return the length of the longest consecutive elements sequence in the array.

For example, the input array [100, 4, 200, 1, 3, 2] has the longest consecutive sequence 1, 2, 3, 4, and thus, you should return its length, 4.
'''

def longest_consecutive(nums):
    sorted_nums = sorted(nums)

    max_length = 1
    tmp_length = 1

    for i in range(1, len(nums)):
        if sorted_nums[i] == sorted_nums[i - 1] + 1:
            tmp_length += 1
            if tmp_length > max_length:
                max_length = tmp_length
        else:
            tmp_length = 1

    return max_length
        

print(longest_consecutive([100, 4, 200, 1, 3, 2, 4, 1]))
# 4