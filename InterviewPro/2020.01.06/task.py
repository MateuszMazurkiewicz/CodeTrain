'''
Given a number of integers, combine them so it would create the largest number.

Example:
Input:  [17, 7, 2, 45, 72]
Output:  77245217
'''

def largestNum(nums):
    s = [str(x) for x in nums]
    permutations = [[]]
    
    for x in s:
        tmp_permutations = []
        new = []
        for permutation in permutations:
            tmp = generate_permutations(permutation, x)
            tmp_permutations += tmp
        
        for p in tmp_permutations:
            if not p in new:
                new.append(p)

        permutations = new.copy()    
        
    values = [int(''.join(x)) for x in permutations]

    return max(values)

def generate_permutations(arr, element):    
    result = []

    for i in range(len(arr) + 1):
        tmp = arr.copy()
        tmp.insert(i, element)        
        result.append(tmp)

    return result

print(largestNum([17, 7, 2, 45, 72]))
# 77245217
