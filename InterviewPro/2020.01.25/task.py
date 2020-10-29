'''
MS Excel column titles have the following pattern: A, B, C, ..., Z, AA, AB, ..., AZ, BA, BB, ..., ZZ, AAA, AAB, ... etc. In other words, column 1 is named "A", column 2 is "B", column 26 is "Z", column 27 is "AA" and so forth. Given a positive integer, find its corresponding column name.
Examples:
Input: 26
Output: Z

Input: 51
Output: AY

Input: 52
Output: AZ

Input: 676
Output: YZ

Input: 702
Output: ZZ

Input: 704
Output: AAB
Here is a starting point:

'''

class Solution:
    def convertToTitle(self, n):
        mapping = [""] + list(map(chr, range(65, 91)))
        k = len(mapping) - 1
        result = ""

        while n > 0:
            index = n % (k)
            if index == 0:
                index = k
            n = (n - index) // k
            result = str(mapping[index]) + result

        return result
  

input1 = 1
input2 = 456976
input3 = 28
print(Solution().convertToTitle(input1))
# A
print(Solution().convertToTitle(input2))
# YYYZ
print(Solution().convertToTitle(input3))
# AB


Input = 26
print(Solution().convertToTitle(Input))
# Output: Z

Input = 51
print(Solution().convertToTitle(Input))
# Output: AY

Input = 52
print(Solution().convertToTitle(Input))
# Output: AZ

Input = 676
print(Solution().convertToTitle(Input))
# Output: YZ

Input = 702
print(Solution().convertToTitle(Input))
# Output: ZZ

Input = 704
print(Solution().convertToTitle(Input))
# Output: AAB