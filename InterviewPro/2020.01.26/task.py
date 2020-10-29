'''
Return the longest run of 1s for a given integer n's binary representation.

Example:
Input: 242
Output: 4
242 in binary is 0b11110010, so the longest run of 1 is 4.
'''

def longest_run(n):
    longest = 0
    tmp_longest = 0

    while n > 0:
        if n & 1 == 1:
            tmp_longest += 1
            longest = max(tmp_longest, longest)
        else:
            tmp_longest = 0

        n = n >> 1

    return longest


print(longest_run(242))
# 4

print(longest_run(0))

print(longest_run(3))

print(longest_run(8))
