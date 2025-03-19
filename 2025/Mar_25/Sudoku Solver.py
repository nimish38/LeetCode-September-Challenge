class Solution:
    def solveSudoku(self, board) -> None:

        def solve():

            def isValid(row, col, char):
                for i in range(9):
                    if board[i][col] == char:
                        return False
                    if board[row][i] == char:
                        return False
                    x, y = (row // 3) + i // 3, (col // 3) + i % 3
                    if board[x][y] == char:
                        return False
                return True

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
        print(board)



