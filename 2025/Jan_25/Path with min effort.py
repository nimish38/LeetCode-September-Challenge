class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n, memo = len(heights), len(heights[0]), []
        for _ in range(m):
            memo.append([-1] * n)

        def solve(i, j):
            if i == m - 1 and j == n - 1:
                return 0
            adj, eff = [(1, 0), (-1, 0), (0, 1), (0, -1)], float('inf')
            val, heights[i][j] = heights[i][j], 'V'
            for a, b in adj:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and heights[x][y] != 'V':
                    eff = min(eff, max(abs(val - heights[x][y]), solve(x, y)))
            heights[i][j] = val
            return eff

        return solve(0, 0)


print(Solution().minimumEffortPath(heights = [[1,2,1,1,1],[1,2,1,2,1],[1,2,1,2,1],[1,2,1,2,1],[1,1,1,2,1]]))