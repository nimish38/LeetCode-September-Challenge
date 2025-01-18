class Solution:
    def countSquares(self, matrix):
        m, n, cnt, memo = len(matrix), len(matrix[0]), 0, []
        for _ in range(m):
            memo.append([0] * n)

        for i in range(m):
            for j in range(n):
                if i == 0 or i == 0:
                    memo[i][j] = matrix[i][j]
                elif matrix[i][j]:
                    memo[i][j] = 1 + min(memo[i][j - 1], memo[i - 1][j], memo[i - 1][j - 1])
                cnt += memo[i][j]
        return cnt


print(Solution().countSquares(matrix = [
    [1,1,0,0,1],
    [1,0,1,1,1],
    [1,1,1,1,1],
    [1,0,1,0,1],
    [0,0,1,0,1]]
))
