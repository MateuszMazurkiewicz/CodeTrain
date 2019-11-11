# There are n people lined up, and each have a height represented as an integer. A murder has happened right in front of them, and only people who are taller than everyone in front of them are able to see what has happened. How many witnesses are there?

# Example:

# Input: [3, 6, 3, 4, 1]  
# Output: 3

# Explanation: Only [6, 4, 1] were able to see in front of them.

 #
 #
 # #
####
####
#####
# 36341                                 x (murder scene)

# Here's your starting point:

def witnesses(heights):
    counter = 0
    people = []
    big_man = heights[-1] -1
    for i in range(len(heights) - 1, -1, -1):
        if heights[i] > big_man:
            counter += 1
            big_man = heights[i]
            people.insert(0, heights[i])
    
    return counter, people

print(witnesses([3, 6, 3, 4, 1]))
# 3