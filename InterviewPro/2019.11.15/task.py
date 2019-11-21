'''
You are given a 2D array of integers. Print out the clockwise spiral traversal of the matrix.

Example:

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

The clockwise spiral traversal of this array is:

1, 2, 3, 4, 5, 10, 15, 20, 19, 18, 17, 16, 11, 6, 7, 8, 9, 14, 13, 12

Here is a starting point:
'''

def matrix_spiral_print(M):
    m = len(M)
    n = len(M[0])

    for i in range(min(m, n)//2 + 1):
        print_rectangle((i, i), (m - i, n - i), M)    

# Fill this in.
def print_rectangle(start, end, M):
    for i in range(start[1], end[1]):
        print(M[start[0]][i])

    for i in range(start[0] + 1, end[0]):
        print(M[i][end[0]])

    for i in range(end[1] - 2, start[1] - 1 , -1):
        print(M[end[0] - 1][i])

    for i in range(end[0] - 2, start[0], -1):
        print(M[i][start[0]])

grid = [[1,  2,  3,  4,  5],
        [6,  7,  8,  9,  10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20]]

#print_rectangle((0, 0), (4, 5), grid)

matrix_spiral_print(grid)
# 1 2 3 4 5 10 15 20 19 18 17 16 11 6 7 8 9 14 13 12