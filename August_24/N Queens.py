class Solution:
    def solveNQueens(self, n: int):
        board, res = [], []
        for _ in range(n):
            board.append([1]*n)

        def solve(row):
            for i in range(n):
                if isAvailable(board[row][i]):
                    board[row][i] = 'Q'
                    if row == n - 1:
                        addanswer(board)
                        return
                    solve(row + 1)
                board[row][i] = '1'

        solve(0)

        return res
