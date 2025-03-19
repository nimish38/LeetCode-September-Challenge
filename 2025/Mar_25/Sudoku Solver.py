class Solution:
    def solveSudoku(self, board) -> None:

        def solve():
            for i in range(9):
                for j in range(9):
                    if board[i][j] == '.':
                        for c in range(1, 10):
                            val = str(c)
                            if isValid(i, j, val):
                                board[i][j] = val
                                if solve(board):
                                    return True
                                board[i][j] = '.'
                        return False
            return True

        solve(board)

