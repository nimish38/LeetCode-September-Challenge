class Solution:
    def numIslands(self, grid) -> int:
        m, n, cnt = len(grid), len(grid[0]), 0

        def dfs(a, b):
            if a < 0 or a >= m or b < 0 or b >= n:
                return
            grid[a][b] = '$'
            adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
            for x, y in adj:
                dfs(a + x, b + y)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt