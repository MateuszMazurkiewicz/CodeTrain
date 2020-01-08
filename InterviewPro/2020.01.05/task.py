'''
Given a string, rearrange the string so that no character next to each other are the same. If no such arrangement is possible, then return None.

Example:
Input: abbccc
Output: cbcbca
'''

def is_valid(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False

    return True

def rearrangeString(s):
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
        
    if not permutations:
        return None

    return ''.join(permutations[0])

def generate_permutations(arr, element):    

    result = []

    for i in range(len(arr) + 1):
        tmp = arr.copy()
        tmp.insert(i, element)
        if is_valid(tmp):
            result.append(tmp)

    return result

print(rearrangeString('abbccc'))
# cbcabc

print(rearrangeString('abbccccc'))