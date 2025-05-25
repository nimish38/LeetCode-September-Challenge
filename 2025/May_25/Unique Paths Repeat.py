class Solution(object):
    def uniquePaths(self, m, n):
        grid = [[1] * m for _ in range(n)]
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[-1][-1]