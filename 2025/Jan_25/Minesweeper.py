class Solution:
    def updateBoard(self, board, click):
        def get_count(r, c):
            rt, rb, cl, cr, cnt = max(0, r - 1), min(len(board), r + 1), max(0, c - 1), min(len(board[0]), c + 1), 0
            for i in range(rt, rb + 1):
                for j in range(cl, cr + 1):
                    if board[i][j] == 'M':
                        cnt += 1
            return cnt

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
        else:
            r, c = click[0], click[1]
            mines = get_count(r, c)
            if mines:
                board[r][c] = str(mines)
            else:
                board[r][c] = 'B'
                rt, rb, cl, cr, cnt = max(0, r - 1), min(len(board), r + 1), max(0, c - 1), min(len(board[0]), c + 1), 0
                for i in range(rt, rb + 1):
                    for j in range(cl, cr + 1):
                        if board[i][j] != 'B':
                            self.updateBoard(board, [i, j])
        return board

