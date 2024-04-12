class Solution:
    def uniquePaths(self, m: int, n: int):
        def findPaths(row, col):
            if col == 0 and row == 0:
                return 0
            if col == 0 or row == 0:
                return 1
            if memo[row][col] == -1:
                memo[row][col] = findPaths(row, col - 1) + findPaths(row - 1, col)
            return memo[row][col]
        if m == 1 or n == 1:
            return 1
        memo = []
        for _ in range(m):
            memo.append([-1]*n)

        return findPaths(m - 1, n - 1)

print(Solution().uniquePaths(m = 3, n = 7))