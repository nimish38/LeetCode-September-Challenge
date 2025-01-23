class Solution:
    def longestIncreasingPath(self, matrix):
        m, n, cnt, memo = len(matrix), len(matrix[0]), 0, []
        for _ in range(m):
            memo.append([-1] * n)

        def solve(i, j):
            if memo[i][j] == -1:
                val, adj, temp = matrix[i][j],[(0, -1), (0, 1), (-1, 0), (1, 0)], 0
                matrix[i][j] = -1
                for a, b in adj:
                    x, y = i + a, j + b
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > val:
                        temp = max(temp, solve(x, y))
                matrix[i][j] = val
                memo[i][j] = 1 + temp
            return memo[i][j]

        for i in range(m):
            for j in range(n):
                cnt = max(cnt, solve(i, j))
        return cnt


print(Solution().longestIncreasingPath(matrix = [[9,9,4],[6,6,8],[2,1,1]]))