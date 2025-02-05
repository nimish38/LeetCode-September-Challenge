class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:

        def solve(r, c, k):
            if r < 0 or r >= n or c < 0 or c >= n:
                return 0
            if k == 0:
                return 1
            res, moves = 0.0, [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
            for i, j in moves:
                res += solve(r + i, c + j, k - 1)
            return res / 8
        return solve(row, column, k)


print(Solution().knightProbability( n = 3, k = 2, row = 0, column = 0))