class Solution:
    def minPathSum(self, grid) -> int:
        m, n = len(grid), len(grid[0])

        def solve(row, col):
            if row < 0 or col < 0:
                return float('inf')
            if row == 0 and col == 0:
                return grid[0][0]
            left = solve(row, col - 1)
            up = solve(row - 1, col)
            return grid[row][col] + min(left, up)

        return solve(m - 1, n - 1)

print(Solution().minPathSum(grid = [[1,2,3],[4,5,6]]))