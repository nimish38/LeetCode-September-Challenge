class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)

        def solve(row, col):
            if col < 0 or col > row:
                return float('inf')
            if row == n - 1:
                return triangle[row][col]
            left = solve(row + 1, col)
            right = solve(row + 1, col + 1)
            return triangle[row][col] + min(left, right)

        return solve(0, 0)

print(Solution().minimumTotal(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]))
