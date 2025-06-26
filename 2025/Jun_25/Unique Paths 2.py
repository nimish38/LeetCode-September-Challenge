class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        if obstacleGrid[-1][-1] or obstacleGrid[0][0]:
            return 0
        m, n, cnt = len(obstacleGrid), len(obstacleGrid[0]), 0
        memo = [[0] * n for _ in range(m)]
        for _ in range(m):
            if obstacleGrid[_][0]:
                break
            memo[_][0] = 1
        for _ in range(n):
            if obstacleGrid[0][_]:
                break
            memo[0][_] = 1

        for i in range(1, m):
            for j in range(1, n):
                if not obstacleGrid[i][j]:
                    memo[i][j] += memo[i - 1][j] + memo[i][j - 1]
        return memo[-1][-1]

print(Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))