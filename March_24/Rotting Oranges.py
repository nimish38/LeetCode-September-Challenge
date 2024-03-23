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
                    stack.append((i, j))

        while stack and good:
            time += 1
            for _ in range(len(stack)):
                item = stack.pop()
                x, y = item[0], item[0]

                for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    i = x + dx
                    j = y + dy

                    if i < 0 or i == col or j == row or j < 0:
                        continue

                    if grid[i][j] == 0 or grid[i][j] == 2:
                

                    stack.append((i, j))
                    grid[i][j] = 2
                    good -= 1

        if good > 0:
            return -1
        return time

print(Solution().orangesRotting(grid = [[2,1,1],[1,1,1],[0,1,2]]))