class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = []
        for _ in range(m):
            memo.append([0]*n)

        for i in range(m):
            if not obstacleGrid[i][0]:
                memo[i][0] = 1

        for i in range(n):
            if not obstacleGrid[0][i]:
                memo[0][i] = 1

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    memo[i][j] = memo[i - 1][j] + memo[i][j - 1]

        return memo[m - 1][n - 1]

print(Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))