class Solution:
    def maxAreaOfIsland(self, grid) -> int:
        m, n, res = len(grid), len(grid[0]), 0

        def solve(i, j):
            cnt, adj, st = 0, [(1, 0), (-1, 0), (0, 1), (0, -1)], [(i, j)]
            grid[i][j] = 'V'
            while st:
                a, b = st.pop()
                cnt += 1
                for x, y in adj:
                    p, q = a + x, b + y
                    if 0 <= p < m and 0 <= q < n and grid[p][q] == 1:
                        st.append((p, q))
                        grid[p][q] = 'V'
            return cnt

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    res = max(res, solve(i, j))
        return res


print(Solution().maxAreaOfIsland(grid = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))