class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n, self.best = len(matrix), len(matrix[0]), 0

        def solve(i, j):
            if i == m or j == n:
                return 0
            right = solve(i, j + 1)
            diag = solve(i + 1, j + 1)
            down = solve(i + 1, j)

            if matrix[i][j]:
                ans = 1 + min(right, down, diag)
                self.best = max(self.best, ans)
                return ans

        solve(0, 0)
        return self.best
        