class Solution:
    def maximalSquare(self, matrix) -> int:
        m, n, self.best, memo = len(matrix), len(matrix[0]), 0, []
        for _ in range(m):
            memo.append([-1]*n)

        for col in range(n):
            memo[m - 1][col] = int(matrix[m - 1][col])
        for row in range(m):
            memo[row][n - 1] = int(matrix[row][n - 1])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                if matrix[i][j] == '1':
                    right = memo[i][j + 1]
                    diag = memo[i + 1][j + 1]
                    down = memo[i + 1][j]
                    ans = 1 + min(right, down, diag)
                    self.best = max(self.best, ans)
                    memo[i][j] = ans
                else:
                    memo[i][j] = 0

        return self.best ** 2

print(Solution().maximalSquare(matrix=[["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))