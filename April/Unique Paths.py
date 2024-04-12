class Solution:
    def uniquePaths(self, m: int, n: int):
        def findPaths(row, col, num):
            if col < n - 1 or row < m - 1:
                return 1

            return findPaths(row, col + 1, num + 1) + findPaths(row + 1, col, num + 1)
        return findPaths(0, 0, 0)

print(Solution().uniquePaths(m = 3, n = 3))