class Solution(object):
    def numIslands(self, grid):
        m, n, cnt = len(grid), len(grid[0]), 0

        def dfs(i,j):
            st, grid[i][j] = [(i, j)], 'V'
            while st:
                a, b = st.pop()
                for u, v in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    x, y = a + u, b + v
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == '1':
                        st.append((x, y))
                        grid[x][y] = 'V'

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    cnt += 1
        return cnt

print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))