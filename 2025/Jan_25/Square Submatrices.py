class Solution:
    def countSquares(self, matrix):
        m, n, cnt, memo = len(matrix), len(matrix[0]), 0, []
        for _ in range(m):
            memo.append([-1] * n)

        def solve(r, c):
            if r >= m or c >= n or not matrix[r][c]:
                return 0
            if memo[r][c] == -1:
                right = solve(r, c + 1)
                down = solve(r + 1, c)
                diag = solve(r + 1, c + 1)
                memo[r][c] = 1 + min(right, down, diag)
            return memo[r][c]

        for i in range(m):
            for j in range(n):
                cnt += solve(i, j)
        return cnt


print(Solution().countSquares(matrix = [
    [1,1,0,0,1],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [0,0,1,0,1]]
))
