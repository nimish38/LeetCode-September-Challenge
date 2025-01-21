class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n, area = len(grid), len(grid[0]), 0

        def dfs(a, b):
            st, cnt, adj = [(a, b)], 0, [(0, -1), (0, 1), (-1, 0), (1, 0)]
            while st:
                i, j = st.pop()
                if 0 <= i < m and 0 <= j < n and grid[i][j]:
                    cnt += 1
                    for x, y in adj:
                        st.append((i + x, j + y))
            return cnt
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    area = max(area, dfs(i, j))
        return area