'''
Given a list of words, and an arbitrary alphabetical order, verify that the words are in order of the alphabetical order.

Example:
Input:
words = ["abcd", "efgh"], order="zyxwvutsrqponmlkjihgfedcba"

Output: False
Explanation: 'e' comes before 'a' so 'efgh' should come before 'abcd'

Example 2:
Input:
words = ["zyx", "zyxw", "zyxwy"],
order="zyxwvutsrqponmlkjihgfedcba"

Output: True
Explanation: The words are in increasing alphabetical order

Here's a starting point:
'''

def word_sorted(word, order):
    word_index = 0
    order_index = 0
    while word_index < len(word) and order_index < len(order):
        while word_index < len(word) and order_index < len(order) and word[word_index] == order[order_index]:
            word_index +=1

        order_index += 1

    return order_index < len(order)

def isSorted(words, order):
    
    max_len = max([len(w) for w in words])
    for i in range(max_len):
        tmp = []
        for word in words:
            if i < len(word):
                tmp.append(word[i])
        
        tmp_word = ''.join(tmp)

        if not word_sorted(tmp_word, order):
            return False

    return True


       
   

print(isSorted(["abcd", "efgh"], "zyxwvutsrqponmlkjihgfedcba"))
# False
print(isSorted(["zyx", "zyxw", "zyxwy"], "zyxwvutsrqponmlkjihgfedcba"))
# True