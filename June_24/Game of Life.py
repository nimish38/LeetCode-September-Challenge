class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])
        lives = []
        def count(row, col):
            live = 0
            if row > 0:
                if board[row - 1][col]:
                    live += 1
            if row < m - 1:
                if board[row + 1][col]:
                    live += 1
            if col > 0:
                if board[row][col - 1]:
                    live += 1
            if col < n - 1:
                if board[row][col + 1]:
                    live += 1
            if row > 0 and col > 0:
                if board[row - 1][col - 1]:
                    live += 1
            if row < m - 1 and col < n - 1:
                if board[row + 1][col + 1]:
                    live += 1
            if row > 0 and col < n - 1:
                if board[row - 1][col + 1]:
                    live += 1
            if row < m - 1 and col > 0:
                if board[row + 1][col - 1]:
                    live += 1
            lives[row].append(live)

        for i in range(m):
            lives.append([])
            for j in range(n):
                count(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j]:
                    if lives[i][j] < 2 or lives[i][j] > 3:
                        board[i][j] = 0
                else:
                    if lives[i][j] == 3:
                        board[i][j] = 1

        print(board)

Solution().gameOfLife(board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]])