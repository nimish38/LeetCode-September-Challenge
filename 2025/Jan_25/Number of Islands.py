class Solution:
    def numIslands(self, grid) -> int:
        m, n, cnt = len(grid), len(grid[0]), 0

        def dfs(p, q):
            st = [(p, q)]
            while st:
                a, b = st.pop()
                grid[a][b] = '$'
                adj = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                for x, y in adj:
                    r, s = a + x, b + y
                    if r >= 0 and r < m and s >= 0 and s < n and grid[r][s] == '1':
                        st.append((r, s))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    dfs(i, j)
        return cnt


print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
))