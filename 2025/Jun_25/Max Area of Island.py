class Solution(object):
    def maxAreaOfIsland(self, grid):
        m, n, best = len(grid), len(grid[0]), 0
        def solve(i, j):
            cnt, st = 1, [(i, j)]
            grid[i][j] = -1
            while st:
                a, b = st.pop()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = a + dx, b + dy
                    if 0 <= x < m and 0 <= y < n and grid[x][y]:
                        grid[x][y] = -1
                        st.append((x, y))
                        cnt += 1
            return cnt
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    best = max(best, solve(i, j))
        return best