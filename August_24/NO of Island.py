from collections import deque
class Solution:
    def numIslands(self, grid) -> int:
        m, n, cnt = len(grid), len(grid[0]), 0

        def dfs(i, j):
            st = [(i, j)]
            while st:
                a, b = st.pop()
                grid[a][b] = 'V'
                if a > 0 and grid[a - 1][b] == '1':
                    st.append((a - 1, b))
                if a < m - 1 and grid[a + 1][b] == '1':
                    st.append((a + 1, b))
                if b > 0 and grid[a][b - 1] == '1':
                    st.append((a, b - 1))
                if b < n - 1 and grid[a][b + 1] == '1':
                    st.append((a, b + 1))

        def bfs(i, j):
            qu = deque([(i, j)])
            while qu:
                a, b = qu.popleft()
                grid[a][b] = 'V'
                if a > 0 and grid[a - 1][b] == '1':
                    qu.append((a - 1, b))
                if a < m - 1 and grid[a + 1][b] == '1':
                    qu.append((a + 1, b))
                if b > 0 and grid[a][b - 1] == '1':
                    qu.append((a, b - 1))
                if b < n - 1 and grid[a][b + 1] == '1':
                    qu.append((a, b + 1))


        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # dfs(i, j)
                    bfs(i, j)
                    cnt += 1
        return cnt

print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))