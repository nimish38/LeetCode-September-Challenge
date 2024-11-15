class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n, self.best = len(matrix), len(matrix[0]), 0

        def solve(i, j):
            if i >= m or j >= n:
                return 0
            right = solve(i, j + 1)
            diag = solve(i + 1, j + 1)
            down = solve(i + 1, j)

            if matrix[i][j] == '1':
                ans = 1 + min(right, down, diag)
                self.best = max(self.best, ans)
                return ans
            else:
                return 0

        solve(0, 0)
        return self.best ** 2

print(Solution().maximalSquare(matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))