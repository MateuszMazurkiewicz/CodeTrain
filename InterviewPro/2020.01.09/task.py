'''
You are given an array of integers. Return all the permutations of this array.
'''
def permute(nums):
    permutations = [[nums[0]]]

    for i in range(1, len(nums)):        
        tmp_permutations = []
        for x in permutations:            
            for j in range(i + 1):
                tmp = x.copy()
                tmp.insert(j, nums[i])
                tmp_permutations.append(tmp)
        permutations = tmp_permutations.copy()

    return permutations


print(permute([1, 2, 3]))
# [[1, 2, 3], [2, 1, 3], [2, 3, 1], [1, 3, 2], [3, 1, 2], [3, 2, 1]]
