class Solution:
    def longestIncreasingPath(self, matrix):
        m, n, cnt = len(matrix), len(matrix[0]), 0

        def solve(i, j):
            val, adj, temp = matrix[i][j],[(0, -1), (0, 1), (-1, 0), (1, 0)], 0
            matrix[i][j] = -1
            for a, b in adj:
                x, y = i + a, j + b
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > val:
                    temp = max(temp, solve(i , j))
            matrix[i][j] = val
            return 1 + temp

        for i in range(m):
            for j in range(n):
                cnt = max(cnt, solve(i, j))
        return cnt
