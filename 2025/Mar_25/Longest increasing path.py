class Solution:
    def longestIncreasingPath(self, matrix) -> int:
        m, n, res, memo = len(matrix), len(matrix[0]), 0, []
        for _ in range(m):
            memo.append([-1]*n)

        def solve(i, j):
            if memo[i][j] == -1:
                curr, adj = 0, [(0, 1), (1, 0), (0, -1), (-1, 0)]
                for p, q in adj:
                    x, y = i + p, j + q
                    if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                        curr = max(curr, solve(x, y))
                memo[i][j] = 1 + curr
            return memo[i][j]

        for i in range(m):
            for j in range(n):
                res = max(res, solve(i, j))
        return res


print(Solution().longestIncreasingPath(matrix = [[3,4,5],[3,2,6],[2,2,1]]))