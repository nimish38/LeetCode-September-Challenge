class Solution:
    def updateBoard(self, board, click):
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            self.st = [(click[0], click[1])]
            while self.st:
                row, col = self.st.pop()
                val = explore(row, col)
                board[row][col] = val
        return board
