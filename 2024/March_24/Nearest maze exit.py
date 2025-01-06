class Solution:
    def nearestExit(self, maze, entrance):
        row = len(maze)
        col = len(maze[0])
        stack = [(entrance, 0)]
        maze[entrance[0]][entrance[1]] = '+'

        while stack:
            item = stack.pop(0)
            x, y = item[0][0], item[0][1]
            if maze[x][y] == 'v' and (x == 0 or x == row - 1 or y == 0 or y == col - 1):
                return item[1]
            else:
                if y > 0 and maze[x][y - 1] == '.':
                    stack.append(([x, y - 1], item[1] + 1))
                    maze[x][y - 1] = 'v'

                if y < col - 1 and maze[x][y + 1] == '.':
                    stack.append(([x, y + 1], item[1] + 1))
                    maze[x][y + 1] = 'v'

                if x > 0 and maze[x - 1][y] == '.':
                    stack.append(([x - 1, y], item[1] + 1))
                    maze[x - 1][y] = 'v'

                if x < row - 1 and maze[x + 1][y] == '.':
                    stack.append(([x + 1, y], item[1] + 1))
                    maze[x + 1][y] = 'v'
        return -1



# print(Solution().nearestExit(maze = [[".","+"]], entrance = [0,0]))