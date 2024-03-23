class Solution:
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])

        stack, good, time = [], 0, 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    good += 1
                if grid[i][j] == 2:
                    stack.append((i, j), time)

        
