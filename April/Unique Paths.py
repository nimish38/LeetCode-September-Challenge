class Solution:
    def uniquePaths(self, m: int, n: int):
        def findPaths(row, col):
            if col == 0 and row == 0:
                return 0
            if col == 0 or row == 0:
                return 1

            return findPaths(row, col - 1) + findPaths(row - 1, col)
        return findPaths(m - 1, n - 1)

print(Solution().uniquePaths(m = 3, n = 3))