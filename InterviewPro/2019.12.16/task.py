'''
You are given an array of integers. Return the length of the longest increasing subsequence (not necessarily contiguous) in the array.

Example:
[0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]

The following input should return 6 since the longest increasing subsequence is 0, 2, 6, 9 , 11, 15.
'''

def longest(nums):
    sq = []    

    for i in range(len(nums)):
        x = nums[i]
        current = [x]
        for j in range(i):

            if len(sq[j]) >= len(current) - 1 and sq[j][-1] < x:                
                current = sq[j] + [x]

        sq.append(current.copy())

    sequence = max(sq, key=lambda x: len(x))

    return len(sequence), sequence


    
print(longest([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]))
