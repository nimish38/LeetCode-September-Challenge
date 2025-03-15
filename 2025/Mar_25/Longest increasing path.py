class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        m, n, res = len(matrix), len(matrix[0]), 0

        def solve(i, j):
            curr, adj = 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
            for p, q in adj:
                x, y = i + p, j + q
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                    curr = max(curr, solve(x, y))
            return 1 + curr

        for i in range(m):
            for j in range(n):
                res = max(res, solve(i, j))
        return res


print(Solution().longestIncreasingPath(matrix = [[1]]))