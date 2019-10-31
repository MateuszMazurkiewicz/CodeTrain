# Given two strings, determine the edit distance between them. 
# The edit distance is defined as the minimum number of edits (insertion, deletion, or substitution) needed to change one string to the other.

# For example, "biting" and "sitting" have an edit distance of 2 (substitute b for s, and insert a t).

# Here's the signature:

def distance(s1, s2):
  # Fill this in.
    return max(len(s1), len(s2)) - find_max_matching(s1, s2)
         
def find_max_matching(s1, s2):
    substrings_list = []

    max_matching = 0

    for index1 in range(len(s1)):
        for index2 in range(len(s2)):
            if s1[index1] == s2[index2]:
                substrings_list.insert(0, [(index1, index2), 1])
                max_matching = 1

    while len(substrings_list) > 0:
        tmp = substrings_list.pop()
        for index1 in range(tmp[0][0] + 1, len(s1)):
            for index2 in range(tmp[0][1] + 1,len(s2)):
                if s1[index1] == s2[index2]:
                    substrings_list.insert(0, [(index1, index2), tmp[1] + 1])
                    if tmp[1] + 1 > max_matching:
                        max_matching = tmp[1] + 1 

    return max_matching


print(find_max_matching('biting', 'sitting'))
# 5

print(distance('biting', 'sitting'))
# 2