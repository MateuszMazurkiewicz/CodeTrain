#Given a string, find the length of the longest substring without repeating characters.

#Here is an example solution in Python language. (Any language is OK to use in an interview, though we'd recommend Python as a generalist language utilized by companies like Google, Facebook, Netflix, Dropbox, Pinterest, Uber, etc.,)

class Solution:
  def lengthOfLongestSubstring(self, s):
    # Fill this in.
    if s is None:
        return 0

    counter = 0
    max_length = 0
    char_set = set()

    for character in s:
        if character in char_set:
            if max_length < counter:
                max_length = counter
            counter = 0
            char_set.clear()
            
        counter += 1
        char_set.add(character)

    if max_length < counter:
        max_length = counter

    return max_length        


print(Solution().lengthOfLongestSubstring('abrkaabcdefghijjxxx'))
# 10