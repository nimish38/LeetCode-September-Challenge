import heapq


class Solution(object):
    def swimInWater(self, grid):
        t, st, m, n = 0, [(grid[0][0], 0, 0)], len(grid), len(grid[0])
        grid[0][0] = 'V'
        while st:
            val, i, j = heapq.heappop(st)
            if val > t:
                t = val
            for a,b in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and grid[x][y] != 'V':
                    heapq.heappush(st, (grid[x][y], x, y))
                    if x == m - 1 and y == n - 1:
                        return max(t, grid[-1][-1])
                    grid[x][y] = 'V'
        return t

print(Solution().swimInWater(grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))