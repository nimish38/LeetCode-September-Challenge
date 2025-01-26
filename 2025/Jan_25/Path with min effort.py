class Solution:
    def minimumEffortPath(self, heights) -> int:
        m, n, memo = len(heights), len(heights[0]), []
        for _ in range(m):
            memo.append([-1] * n)

        def solve(i, j):
            if memo[i][j] == -1:
                if i == m - 1 and j == n - 1:
                    memo[i][j] = 0
                else:
                    adj, eff = [(1, 0), (-1, 0), (0, 1), (0, -1)], float('inf')
                    val, heights[i][j] = heights[i][j], 'V'
                    for a, b in adj:
                        x, y = i + a, j + b
                        if 0 <= x < m and 0 <= y < n and heights[x][y] != 'V':
                            eff = min(eff, max(abs(val - heights[x][y]), solve(x, y)))
                    heights[i][j] = val
                    memo[i][j] = eff
            return memo[i][j]

        return solve(0, 0)


print(Solution().minimumEffortPath(heights = [[2, 3],[4, 2]]))