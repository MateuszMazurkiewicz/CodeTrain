'''
Given an array of characters with repeats, compress it in place. The length after compression should be less than or equal to the original array.

Example:
Input: ['a', 'a', 'b', 'c', 'c', 'c']
Output: ['a', '2', 'b', 'c', '3']
Here's a starting point:
'''

class Solution(object):
    def compress(self, chars):
        i = 0
        res = []

        while i < len(chars):
            current = chars[i]
            counter = 0
            while i < len(chars) and chars[i] == current:
                counter +=1
                i += 1

            res.append(current)
            if counter > 1:
                res.append(str(counter))

        return res

print(Solution().compress(['a', 'a', 'b', 'c', 'c', 'c']))
# ['a', '2', 'b', 'c', '3']