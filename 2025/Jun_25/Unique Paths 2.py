class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n, cnt = len(obstacleGrid), len(obstacleGrid[0]), 0
        memo = [[-1] * n for _ in range(m)]
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                return 1
            if memo[i][j] == -1:
                obstacleGrid[i][j], val = 1, 0
                for x, y in [(1, 0), (0, 1)]:
                    a, b = i + x, j + y
                    if m > a >= 0 and 0 <= b < n and obstacleGrid[a][b] == 0:
                        val += dfs(a, b)
                obstacleGrid[i][j], memo[i][j] = 0, val
            return memo[i][j]
        if not obstacleGrid[0][0]:
            cnt = dfs(0, 0)
        return cnt

print(Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))