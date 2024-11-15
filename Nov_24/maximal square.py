class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n, self.best, memo = len(matrix), len(matrix[0]), 0, []
        for _ in range(m):
            memo.append([-1]*n)

        def solve(i, j):
            if i >= m or j >= n:
                return 0
            if memo[i][j] == -1:
                right = solve(i, j + 1)
                diag = solve(i + 1, j + 1)
                down = solve(i + 1, j)

                if matrix[i][j] == '1':
                    ans = 1 + min(right, down, diag)
                    self.best = max(self.best, ans)
                    memo[i][j] = ans
                else:
                    memo[i][j] = 0
            return memo[i][j]

        solve(0, 0)
        return self.best ** 2

print(Solution().maximalSquare(matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))