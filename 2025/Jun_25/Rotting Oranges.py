from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        m, n, cnt, que, time = len(grid), len(grid[0]), 0, deque(), 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    que.append((i, j))
                if grid[i][j] == 1:
                    cnt += 1
        if cnt == 0:
            return 0
        while que and cnt > 0:
            for _ in range(len(que)):
                a, b = que.popleft()
                for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    x, y = a + dx, b + dy
                    if 0 <= x < m and 0 <=y < n and grid[x][y] == 1:
                        cnt -= 1
                        que.append((x, y))
                        grid[x][y] = 2
                    if cnt == 0:
                        return time + 1
            time += 1
        return -1

print(Solution().orangesRotting(grid = [[2,1,1],[1,1,0],[0,1,1]]))