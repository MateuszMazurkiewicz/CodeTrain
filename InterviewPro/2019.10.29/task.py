# You are given a positive integer N which represents the number of steps in a staircase. 
# You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.
    first = 1
    second = 1

    for _ in range(n):
        tmp = second
        second += first
        first = tmp

    return first

# It is just fibonacci sequence
  
print(staircase(4))
# 5
print(staircase(5))
# 8