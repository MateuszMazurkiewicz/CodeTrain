'''
Given two strings A and B of lowercase letters, return true if and only if we can swap two letters in A so that the result equals B.

Example 1:
Input: A = "ab", B = "ba"
Output: true
Example 2:

Input: A = "ab", B = "ab"
Output: false
Example 3:
Input: A = "aa", B = "aa"
Output: true
Example 4:
Input: A = "aaaaaaabc", B = "aaaaaaacb"
Output: true
Example 5:
Input: A = "", B = "aa"
Output: false
Here's a starting point:
'''

class Solution:
    def buddyStrings(self, A, B):
        if len(A) != len(B):
            return False

        a_letters = []
        b_letters = []
        counter = 0

        for index in range(len(A)):
            if counter > 2:
                  return False
            if A[index] != B[index]:
                a_letters.append(A[index])
                b_letters.append(B[index])
                counter += 1

        if a_letters[0] == b_letters[1] and a_letters[1] == b_letters[0]:
            return True

        return False



print(Solution().buddyStrings('aaaaaaabc', 'aaaaaaacb'))
# True
print(Solution().buddyStrings('aaaaaabbc', 'aaaaaaacb'))
# False