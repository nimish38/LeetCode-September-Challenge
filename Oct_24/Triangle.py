class Solution:
    def minimumTotal(self, triangle) -> int:
        n = len(triangle)

        def solve(row, col):
            if col < 0 or col > row:
                return float('inf')
            if row == n:
                return triangle[row - 1][col - 1]
            left = solve(row + 1, col)
            right = solve(row + 1, col + 1)
            return triangle[row - 1][col - 1] + min(left, right)
        
        return solve(0, 0)
