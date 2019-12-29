'''
Two words can be 'chained' if the last character of the first word is the same as the first character of the second word.

Given a list of words, determine if there is a way to 'chain' all the words in a circle.

Example:

Input: ['eggs', 'karat', 'apple', 'snack', 'tuna']
Output: True

Explanation:
The words in the order of ['apple', 'eggs', 'snack', 'karat', 'tuna'] creates a circle of chained words.

Here's a start:
'''

from collections import defaultdict

def chainedWords(words):
    d = defaultdict(list)
    for w in words:
        d[w[0]].append(w[-1])

    full = [(w[0], w[-1]) for w in words]
    full.append((words[0][0], words[0][-1]))

    

    root = words[0][0]
    return search(root, d, [], full)


def search(root, d, s, full):
    if sorted(s) == sorted(full):
        return True

    res = False

    for item in d[root]:
        new_s = s.copy()
        if (root, item) in new_s and (root, item) != full[0]:
            continue
        new_s.append((root, item))

        res = res or search(item, d, new_s, full)

    return res


print(chainedWords(['eggs', 'karat', 'apple', 'snack', 'tuna']))
# True

print(chainedWords(['eggs', 'xx', 'apple', 'snack', 'tuna']))
# False
