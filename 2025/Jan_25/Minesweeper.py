class Solution:
    def updateBoard(self, board, click):

        def get_count(r, c):
            rt, rb, cl, cr, cnt = max(0, r - 1), min(len(board), r + 1), max(0, c - 1), min(len(board[0]), c + 1), 0
            for i in range(rt, rb + 1):
                for j in range(cl, cr + 1):
                    if i == r and j == c:
                        continue
                    if board[i][j] == 'M':
                        cnt += 1
            return cnt

        def explore(r, c):
            rt, rb, cl, cr = max(0, r - 1), min(len(board), r + 1), max(0, c - 1), min(len(board[0]), c + 1)
            for i in range(rt, rb + 1):
                for j in range(cl, cr + 1):
                    if i == r and j == c:
                        continue
                    val = get_count(i, j)
                    if val == 0:
                        board[i][j] = 'B'
                        self.st.append((i, j))
                    else:
                        board[i][j] = val


        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            self.st = [(click[0], click[1])]
            while self.st:
                row, col = self.st.pop()
                value = explore(row, col)
                board[row][col] = value
        return board
