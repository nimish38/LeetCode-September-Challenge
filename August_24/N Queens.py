class Solution:
    def solveNQueens(self, n: int):
        board, res = [], []
        for _ in range(n):
            board.append([0]*n)

        def solve(chess, row):
            

        for col in range(n):
            board[0][col] = 1
            solve([*board], 0)
            board[0][col] = 0
        return res
