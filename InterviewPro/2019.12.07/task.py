'''
Given a 2-dimensional grid consisting of 1's (land blocks) and 0's (water blocks), count the number of islands present in the grid. The definition of an island is as follows:
1.) Must be surrounded by water blocks.
2.) Consists of land blocks (1's) connected to adjacent land blocks (either vertically or horizontally).
Assume all edges outside of the grid are water.

Example:
Input: 
10001
11000
10110
00000

Output: 3
Here's your starting point:
'''

class Solution(object):
    def inRange(self, grid, r, c):
        numRow, numCol = len(grid), len(grid[0])
        if r < 0 or c < 0 or r >= numRow or c >= numCol:
            return False
        return True

    def numIslands(self, grid):
        len_x = len(grid)
        len_y = len(grid[0])

        n_islands = 0
        for x in range(len_x):
            for y in range(len_y):
                if grid[x][y] == 1:
                    n_islands +=1
                    self.discover_island(x, y, grid)

        return n_islands

    def discover_island(self, x, y, grid):
        stack = []
        stack.append((x, y))
        while len(stack) > 0:
            point = stack.pop()
            x = point[0]
            y = point[1]           
            grid[x][y] = -1
            neighbors = self.get_neighbors(point)
            for ng in neighbors:
                x = ng[0]
                y = ng[1]
                if self.inRange(grid, x, y) and grid[x][y] == 1:
                    stack.append((x, y))


    def get_neighbors(self, point):
        x = point[0]
        y = point[1]
        return[(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

grid = [[1, 1, 0, 0, 0],
        [0, 1, 0, 0, 1],
        [1, 0, 0, 1, 1],
        [0, 0, 0, 0, 0]]
print(Solution().numIslands(grid))
# 3