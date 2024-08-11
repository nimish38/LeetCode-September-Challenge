class Solution:
    def numIslands(self, grid) -> int:
        m,n = len(grid), len(grid[0])
        self.cnt = 0
        def checkneighbors(i, j):
            if i > 0 and grid[i - 1][j] or j > 0 and grid[i][j-2]:
                return
            self.cnt += 1
            return 
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    checkneighbors(i, j)
        return self.cnt