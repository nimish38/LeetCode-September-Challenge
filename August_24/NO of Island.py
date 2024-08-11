class Solution:
    def numIslands(self, grid) -> int:
        m, n, cnt = len(grid), len(grid[0]), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    if ( i > 0 and grid[i - 1][j] == '1' ) or ( j > 0 and grid[i][j - 1] == '1'):
                        continue
                    else:
                        cnt += 1
        return cnt

print(Solution().numIslands(grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]))