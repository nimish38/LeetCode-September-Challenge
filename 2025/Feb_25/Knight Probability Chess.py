class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        memo = {}
        def solve(r, c, k):
            val = str(r) + '_' + str(c) + '_' + str(k)
            if val not in memo:
                if r < 0 or r >= n or c < 0 or c >= n:
                    memo[val] = 0
                elif k == 0:
                    memo[val] = 1
                else:
                    res, moves = 0.0, [(-2, -1), (-1, -2), (1, -2), (2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1)]
                    for i, j in moves:
                        res += solve(r + i, c + j, k - 1)
                    memo[val] = res / 8
            return memo[val]
        return solve(row, column, k)


print(Solution().knightProbability( n = 3, k = 2, row = 0, column = 0))