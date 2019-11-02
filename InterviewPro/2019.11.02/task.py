# Given a sequence of numbers, find the longest sequence that contains only 2 unique numbers.

# Example:

# Input: [1, 3, 5, 3, 1, 3, 1, 5]
# Output: 4

# The longest sequence that contains just 2 unique numbers is [3, 1, 3, 1]

# Here's the solution signature:

def findSequence(seq):
  # Fill this in.
    n = len(seq)
    if n <= 2:
        return n

    max_length = 2
    current_length = 2
    last_number_length = 1

    other = seq[0]
    last = seq[1]

    for i in range(2, n):
        tmp = seq[i]
        if tmp == other or tmp == last:
            current_length += 1
            if tmp == last:
                last_number_length += 1
            else:
                last_number_length = 1
                other = last
                last = tmp
        else:
            other = last
            last = tmp
            current_length = last_number_length + 1
            last_number_length = 1

        if current_length > max_length:
            max_length = current_length

    return max_length    

print(findSequence([1, 3, 5, 3, 1, 3, 1, 5]))
# 4