class Solution:
    def updateBoard(self, board, click):
        def get_count(r, c):
            cnt = 0
            for i in range(r - 1, r + 2):
                for j in range(c - 1, c + 2):
                    if len(board) > i >= 0 and len(board[0]) > j >= 0 and board[i][j] == 'M':
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
                for i in range(r - 1, r + 2):
                    for j in range(c - 1, c + 2):
                        if len(board) > i >= 0 and len(board[0]) > j >= 0 and board[i][j] != 'B':
                            self.updateBoard(board, [i, j])
        return board


print(Solution().updateBoard(board = [["E","E","E","E","E"],["E","E","M","E","E"],["E","E","E","E","E"],["E","E","E","E","E"]], click = [3,0]))