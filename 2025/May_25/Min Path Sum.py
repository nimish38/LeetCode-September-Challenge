class Solution(object):
    def minPathSum(self, grid):
        m, n = len(grid), len(grid[0])
        memo = [[-1] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i + j == 0:
                    memo[i][j] = 0
                    continue
                up, left = float('inf'), float('inf')
                if i > 0:
                    up = memo[i - 1][j] + grid[i - 1][j]
                if j > 0:
                    left = memo[i][j - 1] + grid[i][j - 1]
                memo[i][j] = min(up, left)
        return memo[-1][-1] + grid[-1][-1]


print(Solution().minPathSum(grid = [[1,3,1],[1,5,1],[4,2,1]]))