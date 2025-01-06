class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo, row, col = [], 1, 1
        for _ in range(m):
            memo.append([0]*n)

        if not obstacleGrid[0][0]:
            memo[0][0] = 1

        for i in range(0, m):
            for j in range(0, n):
                if i == 0 and j == 0:
                    continue
                if not obstacleGrid[i][j]:
                    if i == 0:
                        row = 0
                    else:
                        row = memo[i - 1][j]

                    if j == 0:
                        col = 0
                    else:
                        col = memo[i][j - 1]
                    memo[i][j] = row + col

        return memo[m - 1][n - 1]

print(Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,0,0],[0,0,0]]))