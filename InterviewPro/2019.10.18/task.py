#A palindrome is a sequence of characters that reads the same backwards and forwards. Given a string, s, find the longest palindromic substring in s.

#Example:

#Input: "banana"
#Output: "anana"

#Input: "million"
#Output: "illi"

class Solution: 
    def longestPalindrome(self, s):
      # Fill this in.
        n = len(s)
        longest = 0
        tmp = None
        result = None
        for i in range(n):
            tmp = self.find_odd(i, s)
            if tmp[0] > longest:
                longest = tmp[0]
                result = tmp

            tmp = self.find_even(i, s)
            if tmp[0] > longest:
                longest = tmp[0] 
                result = tmp

        return result[1]

    def find_odd(self, i, s):       
        n = len(s)
        final_left = i
        final_right = i       
        left = i - 1
        right = i + 1      
        palindrome_length = 1  
        while left >= 0 and right < n and s[left] == s[right]:
            palindrome_length += 2
            final_left = left
            final_right = right
            left -= 1
            right += 1

        return (palindrome_length, s[final_left:final_right + 1])

    def find_even(self, i, s):
        n = len(s) 
        final_left = 0
        final_right = 0        
        left = i
        right = i + 1      
        palindrome_length = 0  
        while left >= 0 and right < n and s[left] == s[right]:
            palindrome_length += 2
            final_left = left
            final_right = right
            left -= 1
            right += 1

        if palindrome_length == 0:
            return (0, None)

        return (palindrome_length, s[final_left:final_right + 1])

        
# Test program
s = "tracecars"
print(str(Solution().longestPalindrome(s)))
# racecar