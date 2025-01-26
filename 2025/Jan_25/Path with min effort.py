class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n = len(heights), len(heights[0])

        def solve(i, j, par):
            if i == m - 1 and j == n - 1:
                return abs(par - heights[i][j])
            adj, eff = [(1, 0), (-1, 0), (0, 1), (0, -1)], 0
            val, heights[i][j] = heights[i][j], 'V'
            for a, b in adj:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and heights[x][y] != 'V':
                    eff = min(eff, max(abs(par - val), solve(x, y, val)))
            heights[i][j] = val
            return eff


        return solve(0, 0, heights[0][0])
