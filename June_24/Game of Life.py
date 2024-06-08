class Solution:
    def gameOfLife(self, board):
        m, n = len(board), len(board[0])

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
            return live

        for i in range(m):
            for j in range(n):
                lives = count(i, j)
                if board[i][j]:
                    if lives < 2 or lives > 3:
                        board[i][j] = 0
                else:
                    if lives == 3:
                        board[i][j] = 1