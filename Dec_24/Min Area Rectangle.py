class Solution:
    def minimumArea(self, grid) -> int:
        def checksum(col):
            for i in range(len(grid)):
                if grid[i][col] == 1:
                    return False
            return True

        r1, r2, c1, c2 = 0, len(grid) - 1, 0, len(grid[0]) - 1
        while r1 <= r2 and sum(grid[r1]) == 0:
            r1 += 1

        while r2 > r1 and sum(grid[r2]) == 0:
            r2 -= 1

        while c1 <= c2 and checksum(c1):
            c1 += 1

        while c2 > c1 and checksum(c2):
            c2 -= 1

        return max(0, (c2 - c1) * (r2 - r1))