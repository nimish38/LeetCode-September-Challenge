class Solution:
    def orangesRotting(self, grid):
        row = len(grid)
        col = len(grid[0])

        stack, good, time = [], 0, 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    good += 1
                if grid[i][j] == 2:
                    stack.append(([i, j], time))

        while stack and good:
            item = stack.pop()
            i, j = item[0][0], item[0][1]

            if j > 0 and grid[i][j - 1] == 1:
                stack.append(([i, j - 1], item[1] + 1))
                grid[i][j - 1] = 2
                time = max(time, item[1] + 1)
                good -= 1

            if j < col - 1 and grid[i][j + 1] == 1:
                stack.append(([i, j + 1], item[1] + 1))
                grid[i][j + 1] = 2
                time = max(time, item[1] + 1)
                good -= 1

            if i > 0 and grid[i - 1][j] == 1:
                stack.append(([i - 1, j], item[1] + 1))
                grid[i - 1][j] = 2
                time = max(time, item[1] + 1)
                good -= 1

            if i < row - 1 and grid[i + 1][j] == 1:
                stack.append(([i + 1, j], item[1] + 1))
                grid[i + 1][j] = 2
                time = max(time, item[1] + 1)
                good -= 1

        if good > 0:
            return -1
        return time

# print(Solution().orangesRotting(grid = [[0,2]]))