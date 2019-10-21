#Given a sorted array, A, with possibly duplicated elements, find the indices of the first and last occurrences of a target element, x. Return -1 if the target is not found.

#Example:

#Input: A = [1,3,3,5,7,8,9,9,9,15], target = 9
#Output: [6,8]

#Input: A = [100, 150, 150, 153], target = 150
#Output: [1,2]

#Input: A = [1,2,3,4,5,6,10], target = 9
#Output: [-1, -1]

#Here is a function signature example:

class Solution: 
  def getRange(self, arr, target):
    # Fill this in.
    first = -1
    last = -1
    tmp = 0
    n = len(arr)

    for i in range(n):
        if arr[i] == target:
            first = i
            last = i
            tmp = i + 1
            break

    for i in range(tmp, n):
        if arr[i] == target:
            last = i

    return [first, last]
    
    
  
# Test program 
arr = [1, 2, 2, 2, 2, 3, 4, 7, 8, 8] 
x = 2
print(Solution().getRange(arr, x))
# [1, 4]