class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = []

        for i in range(m):
            if not obstacleGrid[i][0]:
                memo[i][0] = 1
            else:
                memo[i][0] = 0

        for i in range(n):
            if not obstacleGrid[0][i]:
                memo[0][i] = 1
            else:
                memo[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]

