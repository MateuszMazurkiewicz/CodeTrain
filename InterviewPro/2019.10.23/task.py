#You are given a list of numbers, and a target number k. Return whether or not there are two numbers in the list that add up to k.

#Example:
#Given [4, 7, 1 , -3, 2] and k = 5,
#return true since 4 + 1 = 5.

def two_sum(input_list, k):
  # Fill this in.
    matching_set = set()
    for item in input_list:
        if item in matching_set:
            return True
        if k - item in matching_set:
            continue
        else:
            matching_set.add(k - item)

    return False

print(two_sum([4,7,4,1,-3,2], 5)) # True
print(two_sum([4,7,1,-3,2], 20)) # False
