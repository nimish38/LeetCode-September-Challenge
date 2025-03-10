class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n, res = len(grid), len(grid[0]), 0

        def solve(i, j):
            cnt, adj, st = 1, [(1, 0), (-1, 0), (0, 1), (0, -1)], [(i, j)]
            while st:
                a, b = st.pop()
                grid[a][b] = 'V'
                cnt += 1
                for x, y in adj:
                    p, q = a + x, b + y
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                        st.append((p, q))
            return cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, solve(i, j))
        return res