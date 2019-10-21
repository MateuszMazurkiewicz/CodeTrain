#Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#An input string is valid if:
#- Open brackets are closed by the same type of brackets.
#- Open brackets are closed in the correct order.
#- Note that an empty string is also considered valid.

#Example:

#Input: "((()))"
#Output: True

#Input: "[()]{}"
#Output: True

#Input: "({[)]"
#Output: False

class Solution:

  #starting_brackets = {'(', '[', '{'}
  #ending_brackets = {')', ']', '}'}
  matched = {')':'(', ']':'[', '}':'{'}

  def isValid(self, s):
    # Fill this in.
    stack = []
    for bracket in s:
      if bracket in self.matched:
        if len(stack) == 0:
          return False
        if stack[-1] == self.matched[bracket]:
          stack.pop()
        else:
          return False
      else:
        stack.append(bracket)       

    return len(stack) == 0  


# Test Program
s = "()(){(())" 
# should return False
print(Solution().isValid(s))

s = ""
# should return True
print(Solution().isValid(s))

s = "([{}])()"
# should return True
print(Solution().isValid(s))