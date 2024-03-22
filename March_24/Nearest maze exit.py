class Solution:
    def nearestExit(self, maze, entrance):
        row = len(maze)
        col = len(maze[0])
        stack = [(entrance, 0)]
        maze[entrance[0]][entrance[1]] = 'v'
        print(stack)

Solution().nearestExit(maze = [["+","+","+"],[".",".","."],["+","+","+"]], entrance = [1,0])