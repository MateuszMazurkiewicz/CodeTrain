'''
Given a non-empty list of words, return the k most frequent words. The output should be sorted from highest to lowest frequency, and if two words have the same frequency, the word with lower alphabetical order comes first. Input will contain only lower-case letters.

Example:

Input: ["daily", "interview", "pro", "pro", 
"for", "daily", "pro", "problems"], k = 2
Output: ["pro", "daily"]
'''

from collections import defaultdict

class Solution(object):
    def topKFrequent(self, words, k):
        d = defaultdict(lambda : 0)

        for w in words:
            d[w] += 1

        l = list(d.items())

        sorted_l = sorted(l, key=lambda x: (-x[1], x[0]))

        res = []
        for i in range(k):
            res.append(sorted_l[i][0])

        return res
        

words = ["daily", "interview", "pro", "pro", "for", "daily", "pro", "problems", "a", "a", "a"]
k = 3
print(Solution().topKFrequent(words, k))
# ['a', 'pro', 'daily']