# You 2 integers n and m representing an n by m grid, determine the number of ways you can get from the top-left to the bottom-right of the matrix y going only right or down.

# Example:
# n = 2, m = 2

# This should return 2, since the only possible routes are:
# Right, down
# Down, right.

# Here's the signature:
import numpy as np

def num_ways(n, m):
  # Fill this in.
    tmp = np.ones((n, m))

    for i in range(1, n):
        for j in range(1, m):
            tmp[i, j] = tmp[i, j - 1] + tmp[i - 1, j]

    return tmp[-1, -1]

print(num_ways(4, 6))
# 2