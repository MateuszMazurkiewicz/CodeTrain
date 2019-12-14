'''
Given a string, you need to reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.

Example 1:


Input: "The cat in the hat"
Output: "ehT tac ni eht tah"

Note: In the string, each word is separated by single space and there will not be any extra space in the string.

Here's a starting point:
'''

class Solution:
    def reverseWords(self, str):
        words = str.split(' ')
        reversed_words = [x[::-1] for x in words]
        res = ' '.join(reversed_words)
        return res
    

print(Solution().reverseWords("The cat in the hat"))
# ehT tac ni eht tah