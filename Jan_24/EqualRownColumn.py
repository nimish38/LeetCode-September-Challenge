class Solution:
    def equalPairs(self, grid):
        rows = {}
        for row in grid:
            row = list(map(str, row))
            strrow = ' '.join(row)
            if strrow in rows:
                rows[strrow] += 1
            else:
                rows[strrow] = 1

        cnt = 0
        for i in range(len(grid)):
            strcol = ''
            for j in range(len(grid)):
                strcol += str(grid[j][i])
                if j < len(grid) - 1:
                    strcol += ' '
            if strcol in rows:
                cnt += rows[strcol]
        return cnt

print(Solution().equalPairs([[11,1],[1,11]]))


