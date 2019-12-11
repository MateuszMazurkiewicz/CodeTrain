'''
Given a list of words, group the words that are anagrams of each other. (An anagram are words made up of the same letters).

Example:

Input: ['abc', 'bcd', 'cba', 'cbd', 'efg']
Output: [['abc', 'cba'], ['bcd', 'cbd'], ['efg']]

Here's a starting point:
'''

import collections

def create_word_signature(word):
    signature = {}
    for letter in word:
        if letter not in signature:
            signature[letter] = 0
        signature[letter] += 1

    return signature

def compare_signatures(s1, s2):
    if set(s1.keys()) != set(s2.keys()):
        return False

    for key in s1.keys():
        if s1[key] != s2[key]:
            return False
    return True

def groupAnagramWords(strs):
    signatures = []
    for word in strs:
        signatures.append(create_word_signature(word))

    res = []
    for i in range(len(strs)):
        if not strs[i]:
            continue
        tmp = []
        tmp.append(strs[i])
        for j in range(i + 1, len(strs)):
            if not strs[j]:
                continue
            v = compare_signatures(signatures[i], signatures[j])
            if v:
                tmp.append(strs[j])
                strs[j] = None
        res.append(tmp)

    return res



print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))
# [['efg'], ['bcd', 'cbd'], ['abc', 'cba']]