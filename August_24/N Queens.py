class Solution:
    def solveNQueens(self, n: int):
        board, res = [], []
        for _ in range(n):
            board.append([1]*n)

        def isAvailable(row, col):
            left = col
            while left >= 0:
                if board[row][left] == 'Q':
                    return False
                left -= 1

            up = row
            while up >= 0:
                if board[up][col] == 'Q':
                    return False
                up -= 1

            lrow, lcol = row, col
            while lrow >= 0 and lcol >= 0:
                if board[lrow][lcol] == 'Q':
                    return False
                lrow -= 1
                lcol -= 1

            urow, rcol = row, col
            while urow >= 0 and rcol < n:
                if board[urow][rcol] == 'Q':
                    return False
                urow -= 1
                rcol += 1

            return True

        def addanswer(chess):
            val = []
            for i in range(n):
                str = ''
                for j in range(n):
                    if chess[i][j] == 'Q':
                        str += 'Q'
                    else:
                        str += '.'
                val.append(str)
            res.append(val)

        def solve(row):
            for i in range(n):
                if isAvailable(row, i):
                    board[row][i] = 'Q'
                    if row == n - 1:
                        addanswer(board)
                        return
                    solve(row + 1)
                board[row][i] = 1

        solve(0)

        return res
