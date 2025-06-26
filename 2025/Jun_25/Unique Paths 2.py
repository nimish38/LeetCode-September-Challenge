class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        m, n, self.cnt = len(obstacleGrid), len(obstacleGrid[0]), 0
        if m == n == 1:
            return 0 if obstacleGrid[0][0] else 1
        def dfs(i, j):
            if i == m - 1 and j == n - 1:
                self.cnt += 1
                return
            obstacleGrid[i][j] = 1
            for x, y in [(1, 0), (0, 1)]:
                a, b = i + x, j + y
                if m > a >= 0 and 0 <= b < n and obstacleGrid[a][b] == 0:
                    dfs(a, b)
            obstacleGrid[i][j] = 0

        dfs(0, 0)
        return self.cnt

print(Solution().uniquePathsWithObstacles(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]))