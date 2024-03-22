class Solution:
    def nearestExit(self, maze, entrance):
        row = len(maze)
        col = len(maze[0])
        stack = [(entrance, 0)]
        maze[entrance[0]][entrance[1]] = 'v'

        if maze[0].count('.') + maze[row - 1].count('.') == 0:
            exitfound = False
            for i in range(1, row - 1):
                if maze[i][0] == '.' or maze[i][col - 1] == '.':
                    exitfound = True
                    break
        if not exitfound:
            return - 1

        while stack:
            item = stack.pop(0)
            x, y = item[0][0], item[0][1]
            if maze[x][y] == '.' and (x == 0 or x == row - 1 or y == 0 or y == col - 1):
                return item[1]
            else:
                if y > 0 and maze[x][y - 1] == '.':
                    stack.append(([x, y - 1], item[1] + 1))

                if y < col - 1 and maze[x][y + 1] == '.':
                    stack.append(([x, y + 1], item[1] + 1))

                if x > 0 and maze[x - 1][y] == '.':
                    stack.append(([x - 1, y], item[1] + 1))

                if x < row - 1 and maze[x + 1][y] == '.':
                    stack.append(([x + 1, y], item[1] + 1))
            maze[x][y] = 'v'
        return -1



# print(Solution().nearestExit(maze = [[".","+"]], entrance = [0,0]))