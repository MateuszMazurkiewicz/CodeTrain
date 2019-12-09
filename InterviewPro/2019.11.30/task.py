'''
You are given a string s, and an integer k. Return the length of the longest substring in s that contains at most k distinct characters.

For instance, given the string:
aabcdefff and k = 3, then the longest substring with 3 distinct characters would be defff. The answer should be 5.

Here's a starting point:
'''

def longest_substring_with_k_distinct_characters(s, k):
    max_length = 0
    index = 0
    word = []
    while index < len(s):
        unique_letters = set()
        j = index
        tmp_length = 0
        word = []
        while j < len(s):
            letter = s[j]
            if  letter not in unique_letters:
                unique_letters.add( letter)

            if len(unique_letters) > k:
                break

            tmp_length += 1
            if tmp_length > max_length:
                max_length = tmp_length

            j += 1
            word.append(letter)
        print("".join(word))
        index += 1

    return max_length


print(longest_substring_with_k_distinct_characters('aabcdefff', 3))
# 5 (because 'defff' has length 5 with 3 characters)
