class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n, area = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = max(area, dfs(i, j))

        return area